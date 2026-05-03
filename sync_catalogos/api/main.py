"""FastAPI app principal.

Levantar:
    uvicorn sync_catalogos.api.main:app --host 0.0.0.0 --port 8000

Configurar via env vars (prefijo SALUD_API_):
    SALUD_API_DB_URL
    SALUD_API_JWT_SECRET    (obligatorio)
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, insert

from .._envfile import load_env
from .auth import _load_user_from_db, decode_token
from .db import all_catalog_names
from .models import api_audit_log, api_metadata
from .routes import admin as admin_router
from .routes import auth as auth_router
from .routes import catalogs as catalogs_router
from .settings import settings

log = logging.getLogger(__name__)

STATIC_DIR = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_env()
    s = settings()
    engine = create_engine(s.db_url, future=True, pool_pre_ping=True)
    app.state.engine = engine
    # Crear tablas API si no existen (idempotente)
    api_metadata.create_all(engine)
    log.info("api.started", extra={"db_url": s.db_url.split("@")[-1]})
    yield
    engine.dispose()


app = FastAPI(
    title="co-salud-catalogos API",
    description=(
        "API REST sobre los catálogos públicos del sector salud en Colombia "
        "sincronizados por `co-salud-catalogos`. Autenticación Bearer JWT, "
        "permisos por catálogo, documentación filtrada según el usuario logueado."
    ),
    version="0.1.0",
    lifespan=lifespan,
    docs_url=None,         # custom /docs abajo
    openapi_url=None,      # custom /openapi.json abajo (dinámico por user)
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings().cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Audit middleware
# ---------------------------------------------------------------------------

@app.middleware("http")
async def audit_middleware(request: Request, call_next):
    response = await call_next(request)
    # Solo loguea endpoints de la API, no estáticos / docs / landing
    path = request.url.path
    SKIP_PREFIXES = ("/static", "/dashboard", "/openapi", "/docs", "/redoc", "/health")
    if path.startswith("/api/") and not path.startswith(SKIP_PREFIXES):
        username = None
        user_id = None
        # Best-effort: decode el bearer token sin DB lookup
        auth_header = request.headers.get("Authorization", "")
        if auth_header.lower().startswith("bearer "):
            try:
                payload = decode_token(auth_header.split(" ", 1)[1].strip())
                username = payload.get("sub")
                user_id = payload.get("uid")
            except Exception:
                pass
        try:
            engine = request.app.state.engine
            with engine.begin() as conn:
                conn.execute(insert(api_audit_log).values(
                    ts=datetime.now(timezone.utc),
                    user_id=user_id,
                    username=username,
                    method=request.method,
                    path=path,
                    status_code=response.status_code,
                    ip=(request.client.host if request.client else None),
                    notes=None,
                ))
        except Exception as e:
            log.warning("audit.write_failed", extra={"error": str(e)})
    return response


# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------

app.include_router(auth_router.router)
app.include_router(catalogs_router.router)
app.include_router(admin_router.router)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok", "version": app.version}


# ---------------------------------------------------------------------------
# OpenAPI dinámico — filtra `name` enum según permisos del bearer token
# ---------------------------------------------------------------------------

def _build_openapi(allowed: list[str] | None) -> dict[str, Any]:
    """Genera spec OpenAPI con `name` (path param) limitado a `allowed`."""
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    if not allowed:
        return schema

    # Inyecta enum en path params {name} de los endpoints de catálogos
    paths = schema.get("paths", {})
    for path, ops in paths.items():
        if "/api/v1/catalogs/{name}" not in path:
            continue
        for op in ops.values():
            if not isinstance(op, dict):
                continue
            for param in op.get("parameters", []):
                if param.get("in") == "path" and param.get("name") == "name":
                    sch = param.setdefault("schema", {})
                    sch["enum"] = sorted(allowed)
                    sch["x-dynamic-allowed"] = True
                    sch["description"] = (
                        sch.get("description", "")
                        + f" — limitado a los {len(allowed)} catálogos del usuario actual."
                    )
    return schema


@app.get("/openapi.json", include_in_schema=False)
async def openapi_json(request: Request):
    """OpenAPI dinámico: si hay bearer token válido, filtra catálogos por permisos."""
    allowed: list[str] | None = None
    auth_header = request.headers.get("Authorization", "")
    if auth_header.lower().startswith("bearer "):
        token = auth_header.split(" ", 1)[1].strip()
        try:
            payload = decode_token(token)
            user_id = payload.get("uid")
            info = _load_user_from_db(request.app.state.engine, user_id) if user_id else None
            if info is not None:
                if info["role"] == "super_admin":
                    allowed = all_catalog_names(request.app.state.engine)
                else:
                    allowed = sorted(info["permissions"])
        except Exception:
            pass  # token inválido → spec sin filtro
    return JSONResponse(_build_openapi(allowed))


@app.get("/docs", include_in_schema=False)
async def custom_swagger():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title + " — Swagger",
        swagger_favicon_url="/static/favicon.ico",
    )


# ---------------------------------------------------------------------------
# Static / dashboard / landing
# ---------------------------------------------------------------------------

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", include_in_schema=False, response_class=HTMLResponse)
async def landing():
    index = STATIC_DIR / "index.html"
    if index.exists():
        return HTMLResponse(index.read_text(encoding="utf-8"))
    return HTMLResponse(
        "<h1>co-salud-catalogos API</h1>"
        "<p>UI no instalada. Endpoints: <a href='/docs'>/docs</a></p>"
    )


@app.get("/dashboard", include_in_schema=False, response_class=HTMLResponse)
async def dashboard():
    page = STATIC_DIR / "dashboard.html"
    if page.exists():
        return HTMLResponse(page.read_text(encoding="utf-8"))
    return HTMLResponse("<p>Dashboard no instalado.</p>", status_code=404)

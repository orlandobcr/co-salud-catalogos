"""Endpoints de consumo de catálogos.

Modelo freemium:
- `/catalogs` y `/catalogs/{name}` (metadata + schema) → ABIERTOS a todos los autenticados.
  Esto permite que un usuario regular EXPLORE la estructura completa del sistema
  (catálogos disponibles, columnas, conteos) sin necesidad de permiso por catálogo.
- `/catalogs/{name}/entries` y `/catalogs/{name}/distinct/...` → GATED.
  Si el usuario no tiene permiso al catálogo, se devuelve 402 Payment Required
  con un body estructurado (`error_code: PERMISSION_REQUIRED`) que el frontend
  usa para renderizar un CTA "habla con comercial".
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import JSONResponse

from ..auth import CurrentUser, get_current_user
from ..db import (
    distinct_values,
    get_catalog_metadata,
    list_all_catalogs,
    query_catalog_entries,
)
from ..models import CatalogDetail, CatalogSummary, EntriesPage
from ..semantic_columns import GEO_PUBLIC_CATALOGS
from ..settings import settings


router = APIRouter(prefix="/api/v1/catalogs", tags=["catalogs"])


# ---------------------------------------------------------------------------
# Freemium gating
# ---------------------------------------------------------------------------

UPGRADE_CTA = {
    "title": "Catálogo premium",
    "message": (
        "Este catálogo requiere una suscripción para acceder a su contenido detallado. "
        "Puedes seguir explorando la estructura y métricas del sistema, pero el detalle "
        "de los registros está reservado a usuarios con permiso."
    ),
    "action_label": "Solicitar acceso",
    "contact_email": "comercial@kashport.com",
    "contact_url": "mailto:comercial@kashport.com?subject=Acceso%20a%20catálogos%20co-salud-catalogos",
}


def _is_geo_public(name: str) -> bool:
    """Catálogos GEO (DIVIPOLA, postales, INVIAS) son públicos en el modelo freemium."""
    return name in GEO_PUBLIC_CATALOGS


def _require_catalog_access_freemium(user: CurrentUser, catalog_name: str) -> None:
    """Si no tiene permiso → lanza 402 con CTA. GEO es siempre público."""
    if user.is_super_admin or _is_geo_public(catalog_name) or catalog_name in user.permissions:
        return
    raise HTTPException(
        status_code=402,
        detail={
            "error_code": "PERMISSION_REQUIRED",
            "catalog": catalog_name,
            "message": UPGRADE_CTA["message"],
            "upgrade_cta": UPGRADE_CTA,
        },
    )


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get(
    "",
    summary="Lista TODOS los catálogos disponibles (estructura abierta)",
    description=(
        "Modelo freemium: la lista completa es siempre visible para usuarios "
        "autenticados. Cada catálogo trae el flag `accessible` indicando si el "
        "usuario actual puede ver su contenido detallado."
    ),
)
def list_catalogs(request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    rows = list_all_catalogs(engine)
    out = []
    for r in rows:
        accessible = (
            user.is_super_admin
            or _is_geo_public(r["name"])
            or r["name"] in user.permissions
        )
        item = CatalogSummary(
            name=r["name"], source=r["source"], source_url=r.get("source_url"),
            row_count=r.get("row_count"), last_synced=r.get("last_synced"),
            table_name=r.get("table_name"),
        ).model_dump()
        item["accessible"] = accessible
        out.append(item)
    return out


@router.get(
    "/{name}",
    response_model=CatalogDetail,
    summary="Metadata + schema inferido (siempre visible al autenticado)",
)
def get_catalog(name: str, request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    meta = get_catalog_metadata(engine, name)
    if meta is None:
        raise HTTPException(status_code=404, detail=f"Catálogo '{name}' no existe")
    accessible = (
        user.is_super_admin
        or _is_geo_public(name)
        or name in user.permissions
    )
    return JSONResponse({
        **CatalogDetail(
            name=meta["name"],
            source=meta["source"],
            source_url=meta.get("source_url"),
            description=meta.get("description"),
            license=meta.get("license"),
            version=meta.get("version"),
            row_count=meta.get("row_count"),
            last_synced=meta.get("last_synced"),
            sha256=meta.get("sha256"),
            notes=meta.get("notes"),
            table_name=meta.get("table_name"),
            schema=meta.get("schema"),
        ).model_dump(by_alias=True, mode="json"),
        "accessible": accessible,
    })


def _parse_filters_from_query(request: Request) -> dict[str, str]:
    """Extrae `filter[col]=val` del query string. Soporta múltiples filtros."""
    out: dict[str, str] = {}
    for k, v in request.query_params.multi_items():
        if k.startswith("filter[") and k.endswith("]"):
            col = k[len("filter["):-1]
            if col and v:
                out[col] = v
    return out


@router.get(
    "/{name}/entries",
    response_model=EntriesPage,
    summary="Filas paginadas del catálogo (con filtros y búsqueda) — GATED",
    description=(
        "Devuelve filas paginadas. Soporta filtros exactos por columna usando "
        "la sintaxis `?filter[col1]=val1&filter[col2]=val2`. Si el usuario no "
        "tiene permiso al catálogo, devuelve 402 con CTA de upgrade."
    ),
)
def get_entries(
    name: str,
    request: Request,
    limit: int = Query(default=100, ge=1, le=5000, description="Filas por página"),
    offset: int = Query(default=0, ge=0),
    q: str | None = Query(None, description="Búsqueda parcial en columnas de texto"),
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine
    meta = get_catalog_metadata(engine, name)
    if meta is None:
        raise HTTPException(status_code=404, detail=f"Catálogo '{name}' no existe")
    _require_catalog_access_freemium(user, name)

    table_name = meta.get("table_name")
    if not table_name:
        raise HTTPException(
            status_code=409,
            detail="El catálogo está registrado pero su tabla no existe en la DB. Ejecutar sync con --db.",
        )

    filters = _parse_filters_from_query(request)
    s = settings()
    limit = min(limit, s.page_size_max)
    total, rows = query_catalog_entries(
        engine, table_name,
        limit=limit, offset=offset,
        filters=filters or None, search_text=q,
    )
    return EntriesPage(catalog=name, total=total, limit=limit, offset=offset, entries=rows)


@router.get(
    "/{name}/distinct/{column}",
    summary="DISTINCT values de una columna (alimenta dropdowns en cascada) — GATED",
    description=(
        "Devuelve los valores distintos de una columna respetando filtros previos "
        "(`?filter[col1]=val1`). Si el catálogo es público (DIVIPOLA, postales, "
        "INVIAS) NO requiere permiso. El resto está gated."
    ),
)
def get_distinct(
    name: str,
    column: str,
    request: Request,
    q: str | None = Query(None, description="Filtro parcial sobre los valores"),
    limit: int = Query(default=500, ge=1, le=5000),
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine
    meta = get_catalog_metadata(engine, name)
    if meta is None:
        raise HTTPException(status_code=404, detail=f"Catálogo '{name}' no existe")
    _require_catalog_access_freemium(user, name)

    table_name = meta.get("table_name")
    if not table_name:
        return {"catalog": name, "column": column, "values": []}
    filters = _parse_filters_from_query(request)
    values = distinct_values(
        engine, table_name, column,
        filters=filters or None, search_text=q, limit=limit,
    )
    return {
        "catalog": name,
        "column": column,
        "filters": filters,
        "count": len(values),
        "values": values,
    }

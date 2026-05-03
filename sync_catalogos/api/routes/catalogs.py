"""Endpoints de consumo de catálogos."""

from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from ..auth import CurrentUser, get_current_user
from ..db import get_catalog_metadata, list_catalogs_for_user, query_catalog_entries
from ..models import CatalogDetail, CatalogSummary, EntriesPage
from ..settings import settings


router = APIRouter(prefix="/api/v1/catalogs", tags=["catalogs"])


def _allowed_set(user: CurrentUser) -> set[str] | None:
    """None significa 'sin filtro' (super_admin)."""
    return None if user.is_super_admin else user.permissions


@router.get(
    "",
    response_model=list[CatalogSummary],
    summary="Lista catálogos visibles para el usuario actual",
)
def list_catalogs(request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    rows = list_catalogs_for_user(engine, allowed=_allowed_set(user))
    return [
        CatalogSummary(
            name=r["name"], source=r["source"], source_url=r.get("source_url"),
            row_count=r.get("row_count"), last_synced=r.get("last_synced"),
            table_name=r.get("table_name"),
        )
        for r in rows
    ]


@router.get(
    "/{name}",
    response_model=CatalogDetail,
    summary="Metadata + schema inferido de un catálogo",
)
def get_catalog(name: str, request: Request, user: CurrentUser = Depends(get_current_user)):
    if not user.can_access(name):
        raise HTTPException(status_code=403, detail=f"Sin permiso para '{name}'")
    engine = request.app.state.engine
    meta = get_catalog_metadata(engine, name)
    if meta is None:
        raise HTTPException(status_code=404, detail=f"Catálogo '{name}' no existe")
    return CatalogDetail(
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
    )


@router.get(
    "/{name}/entries",
    response_model=EntriesPage,
    summary="Filas paginadas del catálogo (con filtros y búsqueda)",
)
def get_entries(
    name: str,
    request: Request,
    limit: int = Query(default=100, ge=1, le=5000, description="Filas por página"),
    offset: int = Query(default=0, ge=0),
    q: Optional[str] = Query(None, description="Búsqueda parcial en columnas de texto"),
    user: CurrentUser = Depends(get_current_user),
):
    if not user.can_access(name):
        raise HTTPException(status_code=403, detail=f"Sin permiso para '{name}'")
    engine = request.app.state.engine
    meta = get_catalog_metadata(engine, name)
    if meta is None:
        raise HTTPException(status_code=404, detail=f"Catálogo '{name}' no existe")
    table_name = meta.get("table_name")
    if not table_name:
        raise HTTPException(
            status_code=409,
            detail="El catálogo está registrado pero su tabla no existe en la DB. Ejecutar sync con --db.",
        )

    s = settings()
    limit = min(limit, s.page_size_max)
    total, rows = query_catalog_entries(
        engine, table_name, limit=limit, offset=offset, search_text=q,
    )
    return EntriesPage(catalog=name, total=total, limit=limit, offset=offset, entries=rows)

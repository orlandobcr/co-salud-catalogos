"""Cliente Socrata para datos.gov.co.

La SODA API expone cada dataset en:
    https://www.datos.gov.co/resource/{dataset_id}.json
con `$limit` + `$offset` para paginación (máx ~50k por request) y
`$select=count(*)` para total.

App tokens son opcionales pero suben el rate limit de ~1k/hora a
~100k/hora. Configurar `SALUD_SOCRATA_APP_TOKEN` en el ambiente.
"""

from __future__ import annotations

import os
from typing import Any

import httpx

SOCRATA_BASE = "https://www.datos.gov.co/resource"
SOCRATA_PAGE_SIZE = 50_000
USER_AGENT = "co-salud-catalogos/0.1 (Colombia public health catalogs sync)"


def _headers() -> dict[str, str]:
    h = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    token = os.environ.get("SALUD_SOCRATA_APP_TOKEN", "").strip()
    if token:
        h["X-App-Token"] = token
    return h


def fetch_all(
    dataset_id: str,
    *,
    where: str | None = None,
    page_size: int = SOCRATA_PAGE_SIZE,
    progress_cb=None,
) -> list[dict[str, Any]]:
    """Descarga todas las filas de un dataset Socrata vía $limit/$offset."""
    url = f"{SOCRATA_BASE}/{dataset_id}.json"
    out: list[dict[str, Any]] = []
    offset = 0
    with httpx.Client(timeout=120, headers=_headers()) as c:
        while True:
            params = {
                "$limit": str(page_size),
                "$offset": str(offset),
                "$order": ":id",
            }
            if where:
                params["$where"] = where
            r = c.get(url, params=params)
            r.raise_for_status()
            page = r.json()
            if not page:
                break
            out.extend(page)
            if progress_cb is not None:
                progress_cb(len(out))
            if len(page) < page_size:
                break
            offset += page_size
    return out


def metadata_view(dataset_id: str) -> dict[str, Any]:
    """Metadata del dataset (`rowsUpdatedAt`, etc.)."""
    url = f"https://www.datos.gov.co/api/views/{dataset_id}.json"
    with httpx.Client(timeout=30, headers=_headers()) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.json()


def remote_version(dataset_id: str) -> str | None:
    """Best-effort: lee `rowsUpdatedAt` (UNIX seconds) y retorna ISO-8601."""
    try:
        meta = metadata_view(dataset_id)
    except Exception:
        return None
    ts = meta.get("rowsUpdatedAt") or meta.get("dataUpdatedAt") or meta.get("indexUpdatedAt")
    if not ts:
        return None
    try:
        from datetime import UTC, datetime
        return datetime.fromtimestamp(int(ts), tz=UTC).isoformat()
    except Exception:
        return None

"""Helpers para consultar tablas de catálogos dinámicamente desde la DB."""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from sqlalchemy import MetaData, Table, func, select, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import NoSuchTableError


def list_catalogs_for_user(engine: Engine, *, allowed: set[str] | None = None) -> list[dict]:
    """Lista de catálogos con metadata. Si `allowed` es None → todos (super_admin)."""
    sql = text("""
        SELECT name, description, source, source_url, source_id, version, license,
               row_count, last_synced, sha256, notes, table_name
        FROM salud_catalog_metadata
        ORDER BY name
    """)
    out: list[dict] = []
    with engine.connect() as conn:
        for row in conn.execute(sql):
            d = dict(row._mapping)
            if allowed is not None and d["name"] not in allowed:
                continue
            out.append(d)
    return out


def get_catalog_metadata(engine: Engine, name: str) -> dict | None:
    sql = text("""
        SELECT name, description, source, source_url, source_id, version, license,
               row_count, last_synced, sha256, notes, table_name, schema_json
        FROM salud_catalog_metadata
        WHERE name = :name
    """)
    with engine.connect() as conn:
        row = conn.execute(sql, {"name": name}).first()
        if not row:
            return None
        d = dict(row._mapping)
    if d.get("schema_json"):
        try:
            d["schema"] = json.loads(d["schema_json"])
        except Exception:
            d["schema"] = None
    else:
        d["schema"] = None
    d.pop("schema_json", None)
    return d


def reflect_catalog_table(engine: Engine, table_name: str) -> Table | None:
    """Refleja la tabla del catálogo desde la DB. None si no existe."""
    md = MetaData()
    try:
        return Table(table_name, md, autoload_with=engine)
    except NoSuchTableError:
        return None
    except Exception:
        return None


def query_catalog_entries(
    engine: Engine,
    table_name: str,
    *,
    limit: int = 100,
    offset: int = 0,
    filters: dict[str, str] | None = None,
    search_text: str | None = None,
) -> tuple[int, list[dict]]:
    """Consulta paginada sobre la tabla del catálogo. Devuelve (total, rows)."""
    table = reflect_catalog_table(engine, table_name)
    if table is None:
        return 0, []

    stmt = select(table)
    if filters:
        for col_name, value in filters.items():
            if col_name in table.c:
                stmt = stmt.where(table.c[col_name] == value)
    if search_text:
        # Búsqueda parcial en columnas de texto (ILIKE para Postgres, LIKE general)
        like = f"%{search_text}%"
        text_cols = [c for c in table.c if str(c.type).lower().startswith(("varchar", "text", "string"))]
        if text_cols:
            from sqlalchemy import or_
            stmt = stmt.where(or_(*[c.like(like) for c in text_cols]))

    # Total con misma WHERE
    count_stmt = select(func.count()).select_from(stmt.subquery())

    stmt = stmt.order_by(table.c._idx).limit(limit).offset(offset)

    with engine.connect() as conn:
        total = conn.execute(count_stmt).scalar() or 0
        rows = conn.execute(stmt).all()

    out: list[dict] = []
    for r in rows:
        m = dict(r._mapping)
        # Coerce datetimes para JSON-friendly
        for k, v in list(m.items()):
            if isinstance(v, datetime):
                m[k] = v.isoformat()
        out.append(m)
    return total, out


def catalog_exists(engine: Engine, name: str) -> bool:
    sql = text("SELECT 1 FROM salud_catalog_metadata WHERE name = :name")
    with engine.connect() as conn:
        return conn.execute(sql, {"name": name}).first() is not None


def all_catalog_names(engine: Engine) -> list[str]:
    """Para el endpoint de admin: opciones de catálogos a otorgar permiso."""
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT name FROM salud_catalog_metadata ORDER BY name")).all()
    return [r.name for r in rows]

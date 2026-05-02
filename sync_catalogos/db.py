"""DB sinks — escribe catálogos a un motor de persistencia opcional.

Soporta 5 motores via factory `make_sink(url)`:

    - sqlite:///./salud.db                             → SqlSink (SQLAlchemy)
    - postgresql+psycopg://u:p@h:5432/db               → SqlSink
    - mysql+pymysql://u:p@h:3306/db                    → SqlSink
    - mssql+pyodbc://u:p@h/db?driver=ODBC+Driver+18    → SqlSink
    - mongodb://u:p@h:27017/db   |  mongodb+srv://...  → MongoSink (pymongo)

Esquema (paridad entre SQL y Mongo):

    Tabla/Collection 1: salud_catalog_metadata
        documento/fila único por catálogo, con metadata.
    Tabla/Collection 2: salud_catalog_entries
        N documentos/filas, uno por entry. PK = (catalog_name, idx).

Estrategia de upsert: DELETE+INSERT atómico por catálogo. Idempotente.

Drivers requeridos (instalar el extra):
    uv pip install -e ".[postgres]"   # SQLAlchemy + psycopg
    uv pip install -e ".[mysql]"      # SQLAlchemy + pymysql
    uv pip install -e ".[mssql]"      # SQLAlchemy + pyodbc
    uv pip install -e ".[mongo]"      # pymongo
    uv pip install -e ".[db]"         # solo SQLAlchemy (suficiente para sqlite)
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Protocol
from urllib.parse import urlparse

from .schema import CatalogFile

_BATCH_SIZE = 1000


def _parse_iso(ts: str | None) -> datetime | None:
    if not ts:
        return None
    s = ts.rstrip("Z")
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt


class DbSink(Protocol):
    """Interfaz común para todos los sinks de persistencia."""

    def ensure_schema(self) -> None: ...
    def write_catalog(self, catalog: CatalogFile) -> None: ...
    def close(self) -> None: ...


# =====================================================================
# SQL backend (SQLAlchemy 2.x — sqlite / postgres / mysql / mssql)
# =====================================================================

class SqlSink:
    def __init__(self, url: str, *, echo: bool = False) -> None:
        try:
            from sqlalchemy import (
                JSON,
                Column,
                DateTime,
                Index,
                Integer,
                MetaData,
                PrimaryKeyConstraint,
                String,
                Table,
                Text,
                create_engine,
            )
        except ImportError as e:
            raise RuntimeError(
                "SQLAlchemy no está instalado. Instala con:\n"
                "  uv pip install -e \".[db]\"        # solo SQLAlchemy\n"
                "  uv pip install -e \".[postgres]\"  # + psycopg\n"
                "  uv pip install -e \".[mysql]\"     # + pymysql\n"
                "  uv pip install -e \".[mssql]\"     # + pyodbc"
            ) from e

        self.url = url
        self.engine = create_engine(url, future=True, echo=echo)
        md = MetaData()
        self._md = md
        self.t_meta = Table(
            "salud_catalog_metadata", md,
            Column("name", String(120), primary_key=True),
            Column("description", Text),
            Column("source", String(40), nullable=False),
            Column("source_url", Text),
            Column("source_id", String(255)),
            Column("version", String(120)),
            Column("license", Text),
            Column("row_count", Integer),
            Column("last_synced", DateTime(timezone=True)),
            Column("sha256", String(64)),
            Column("notes", Text),
        )
        self.t_entries = Table(
            "salud_catalog_entries", md,
            Column("catalog_name", String(120), nullable=False),
            Column("idx", Integer, nullable=False),
            Column("data", JSON, nullable=False),
            PrimaryKeyConstraint("catalog_name", "idx"),
            Index("ix_salud_catalog_entries_name", "catalog_name"),
        )

    def ensure_schema(self) -> None:
        self._md.create_all(self.engine)

    def write_catalog(self, catalog: CatalogFile, *, batch_size: int = _BATCH_SIZE) -> None:
        from sqlalchemy import delete, insert
        m = catalog.metadata
        entries = catalog.entries or []
        meta_row = {
            "name": m.name,
            "description": m.description or None,
            "source": m.source,
            "source_url": m.source_url or None,
            "source_id": m.source_id,
            "version": m.version,
            "license": m.license or None,
            "row_count": m.row_count if m.row_count is not None else len(entries),
            "last_synced": _parse_iso(m.last_synced),
            "sha256": m.sha256,
            "notes": m.notes or None,
        }
        with self.engine.begin() as conn:
            conn.execute(delete(self.t_entries).where(self.t_entries.c.catalog_name == m.name))
            conn.execute(delete(self.t_meta).where(self.t_meta.c.name == m.name))
            conn.execute(insert(self.t_meta).values(**meta_row))
            if entries:
                ins = insert(self.t_entries)
                rows: list[dict] = []
                for i, entry in enumerate(entries):
                    rows.append({"catalog_name": m.name, "idx": i, "data": entry})
                    if len(rows) >= batch_size:
                        conn.execute(ins, rows)
                        rows.clear()
                if rows:
                    conn.execute(ins, rows)

    def close(self) -> None:
        self.engine.dispose()


# =====================================================================
# Mongo backend (pymongo)
# =====================================================================

class MongoSink:
    def __init__(self, url: str, *, db_name: str | None = None) -> None:
        try:
            from pymongo import MongoClient
        except ImportError as e:
            raise RuntimeError(
                "pymongo no está instalado. Instala con:\n"
                "  uv pip install -e \".[mongo]\""
            ) from e

        self.url = url
        # DB name: prioriza arg, luego path de la URL, luego default.
        if db_name is None:
            parsed = urlparse(url)
            db_name = (parsed.path or "/salud_catalogos").lstrip("/") or "salud_catalogos"
        self._client: "MongoClient" = MongoClient(url)
        self.db = self._client[db_name]
        self.col_meta = self.db["salud_catalog_metadata"]
        self.col_entries = self.db["salud_catalog_entries"]

    def ensure_schema(self) -> None:
        # Index único en metadata.name (PK lógica)
        self.col_meta.create_index("name", unique=True)
        # Compound PK lógico en entries
        self.col_entries.create_index(
            [("catalog_name", 1), ("idx", 1)], unique=True
        )
        self.col_entries.create_index("catalog_name")

    def write_catalog(self, catalog: CatalogFile, *, batch_size: int = _BATCH_SIZE) -> None:
        from pymongo import InsertOne
        m = catalog.metadata
        entries = catalog.entries or []
        meta_doc = {
            "name": m.name,
            "description": m.description or None,
            "source": m.source,
            "source_url": m.source_url or None,
            "source_id": m.source_id,
            "version": m.version,
            "license": m.license or None,
            "row_count": m.row_count if m.row_count is not None else len(entries),
            "last_synced": _parse_iso(m.last_synced),
            "sha256": m.sha256,
            "notes": m.notes or None,
        }

        # Replace strategy (Mongo no es transaccional sin replica set, pero el
        # delete + insert es secuencial y idempotente — segundo run repite estado).
        self.col_entries.delete_many({"catalog_name": m.name})
        self.col_meta.replace_one({"name": m.name}, meta_doc, upsert=True)

        if entries:
            ops = []
            for i, entry in enumerate(entries):
                ops.append(InsertOne({
                    "catalog_name": m.name,
                    "idx": i,
                    "data": entry,
                }))
                if len(ops) >= batch_size:
                    self.col_entries.bulk_write(ops, ordered=False)
                    ops.clear()
            if ops:
                self.col_entries.bulk_write(ops, ordered=False)

    def close(self) -> None:
        self._client.close()


# =====================================================================
# Factory
# =====================================================================

def make_sink(url: str) -> DbSink:
    """Construye el sink correcto según el prefijo de la URL.

    Levanta `RuntimeError` si el driver requerido no está instalado, con
    mensaje accionable indicando qué extra instalar.
    """
    scheme = url.split(":", 1)[0].lower()
    if scheme.startswith("mongodb"):
        return MongoSink(url)
    # Por defecto, SQLAlchemy maneja sqlite, postgresql, mysql, mssql, oracle, etc.
    return SqlSink(url)

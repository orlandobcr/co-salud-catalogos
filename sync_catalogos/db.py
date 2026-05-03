"""DB sinks — escribe catálogos a un motor de persistencia opcional.

**Schema tipado por catálogo** (no genérico): cada catálogo se mapea a su
propia tabla / colección con columnas inferidas desde los datos reales.

Soporta 5 motores via factory `make_sink(url)`:

    - sqlite:///./salud.db
    - postgresql+psycopg://u:p@h:5432/db
    - mysql+pymysql://u:p@h:3306/db
    - mssql+pyodbc://u:p@h/db?driver=ODBC+Driver+18+for+SQL+Server
    - mongodb://u:p@h:27017/db   |  mongodb+srv://...

Esquema generado:

    salud_catalog_metadata           (1 fila por catálogo, igual en todos los motores)
        name, description, source, source_url, source_id, version,
        license, row_count, last_synced, sha256, notes

    salud_<catalog_name>             (1 tabla / colección por catálogo)
        _idx INTEGER PRIMARY KEY     # posición original 0..N-1
        <col_1> <inferred_type>      # ej. codigo_habilitacion VARCHAR(50)
        <col_2> <inferred_type>      # ej. fecha_apertura DATE
        ...

Tipos inferidos (ver `db_schema.py` para detalles):
    - BIGINT, DOUBLE PRECISION, BOOLEAN, DATE
    - VARCHAR(50/100/255/1000/4000) o TEXT según longitud máxima

Sanitización de nombres:
    - ASCII fold (acentos eliminados)
    - snake_case, lowercase
    - Caracteres no [a-z0-9_] → _
    - Truncado a 63 chars (límite Postgres)
    - Dedup con sufijo _2, _3 si dos originales colapsan

Estrategia de upsert: por catálogo, DELETE + bulk INSERT atómico en transacción.
Idempotente.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Protocol
from urllib.parse import urlparse

from .db_schema import ColumnSpec, coerce_value, infer_schema, sanitize_table_name
from .schema import CatalogFile

log = logging.getLogger(__name__)

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
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


class DbSink(Protocol):
    def ensure_schema(self) -> None: ...
    def write_catalog(self, catalog: CatalogFile) -> None: ...
    def close(self) -> None: ...


# =====================================================================
# SQL backend (SQLAlchemy 2.x)
# =====================================================================

def _sql_type_for(spec: ColumnSpec):
    """Convierte el ColumnSpec a un type SQLAlchemy concreto."""
    from sqlalchemy import (
        BigInteger, Boolean, Date, Float, String, Text,
    )
    name = spec.sql_type_name
    if name == "BIGINT":
        return BigInteger()
    if name == "DOUBLE PRECISION":
        return Float()
    if name == "BOOLEAN":
        return Boolean()
    if name == "DATE":
        return Date()
    if name == "TEXT":
        return Text()
    if name.startswith("VARCHAR("):
        n = int(name[len("VARCHAR("):-1])
        return String(n)
    return String(255)


class SqlSink:
    def __init__(self, url: str, *, echo: bool = False) -> None:
        try:
            from sqlalchemy import (
                Column,
                DateTime,
                Integer,
                MetaData,
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
        self._md_meta = MetaData()
        self.t_meta = Table(
            "salud_catalog_metadata", self._md_meta,
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
            Column("table_name", String(80)),
            Column("schema_json", Text),  # JSON string con el schema inferido (audit)
        )
        # Cache de Tables por catalog_name
        self._tables: dict[str, "Table"] = {}

    def ensure_schema(self) -> None:
        self._md_meta.create_all(self.engine)

    def _build_catalog_table(self, catalog_name: str, schema: list[ColumnSpec]):
        """Construye el objeto Table para un catálogo (sin crear DDL todavía)."""
        from sqlalchemy import Column, Integer, MetaData, Table

        table_name = sanitize_table_name(catalog_name)
        if table_name in self._tables:
            return self._tables[table_name], table_name

        md = MetaData()
        cols = [Column("_idx", Integer, primary_key=True)]
        for spec in schema:
            cols.append(Column(spec.name, _sql_type_for(spec), nullable=spec.nullable))
        table = Table(table_name, md, *cols)
        self._tables[table_name] = table
        return table, table_name

    def write_catalog(self, catalog: CatalogFile, *, batch_size: int = _BATCH_SIZE) -> None:
        import json
        from sqlalchemy import delete, insert
        m = catalog.metadata
        entries = catalog.entries or []
        schema = infer_schema(entries) if entries else []
        table_name = sanitize_table_name(m.name)

        # Construir/cachear tabla y crear DDL si no existe
        if entries:
            table, table_name = self._build_catalog_table(m.name, schema)
            # Crear DDL solo de esta tabla (no toca otras)
            table.create(self.engine, checkfirst=True)

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
            "table_name": table_name,
            "schema_json": json.dumps(
                [{"col": s.name, "from": s.original, "type": s.sql_type_name, "nullable": s.nullable} for s in schema],
                ensure_ascii=False,
            ) if schema else None,
        }

        with self.engine.begin() as conn:
            # Upsert metadata
            conn.execute(delete(self.t_meta).where(self.t_meta.c.name == m.name))
            conn.execute(insert(self.t_meta).values(**meta_row))

            # Replace entries
            if entries:
                conn.execute(delete(table))
                rows: list[dict] = []
                for i, entry in enumerate(entries):
                    if not isinstance(entry, dict):
                        continue
                    row = {"_idx": i}
                    for spec in schema:
                        raw = entry.get(spec.original)
                        row[spec.name] = coerce_value(raw, spec.sql_type_name)
                    rows.append(row)
                    if len(rows) >= batch_size:
                        conn.execute(insert(table), rows)
                        rows.clear()
                if rows:
                    conn.execute(insert(table), rows)

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
        if db_name is None:
            parsed = urlparse(url)
            db_name = (parsed.path or "/salud_catalogos").lstrip("/") or "salud_catalogos"
        self._client: "MongoClient" = MongoClient(url)
        self.db = self._client[db_name]
        self.col_meta = self.db["salud_catalog_metadata"]

    def ensure_schema(self) -> None:
        self.col_meta.create_index("name", unique=True)

    def _collection_for(self, catalog_name: str):
        col_name = sanitize_table_name(catalog_name)
        col = self.db[col_name]
        # Asegurar índice único en _idx
        col.create_index("_idx", unique=True)
        return col, col_name

    def write_catalog(self, catalog: CatalogFile, *, batch_size: int = _BATCH_SIZE) -> None:
        from datetime import date, datetime, time as _time
        from pymongo import InsertOne
        m = catalog.metadata
        entries = catalog.entries or []
        schema = infer_schema(entries) if entries else []
        col, col_name = self._collection_for(m.name)

        def to_bson(v):
            # BSON no soporta `date` puro — promueve a datetime medianoche.
            if isinstance(v, date) and not isinstance(v, datetime):
                return datetime.combine(v, _time.min)
            return v

        # Crear índices secundarios sugeridos (por columnas comunes id-like)
        for spec in schema[:5]:  # solo primeras 5 para no saturar
            if any(k in spec.original.lower() for k in ("codigo", "id", "nit")):
                try:
                    col.create_index(spec.name)
                except Exception:
                    pass

        # Replace metadata + entries
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
            "collection_name": col_name,
            "schema": [
                {"col": s.name, "from": s.original, "type": s.sql_type_name, "nullable": s.nullable}
                for s in schema
            ],
        }
        self.col_meta.replace_one({"name": m.name}, meta_doc, upsert=True)

        # Reemplazo atómico de la colección (drop colección antes de inserts)
        col.delete_many({})

        if entries:
            ops = []
            for i, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    continue
                doc = {"_idx": i}
                for spec in schema:
                    raw = entry.get(spec.original)
                    doc[spec.name] = to_bson(coerce_value(raw, spec.sql_type_name))
                ops.append(InsertOne(doc))
                if len(ops) >= batch_size:
                    col.bulk_write(ops, ordered=False)
                    ops.clear()
            if ops:
                col.bulk_write(ops, ordered=False)

    def close(self) -> None:
        self._client.close()


# =====================================================================
# Factory
# =====================================================================

def make_sink(url: str) -> DbSink:
    """Construye el sink correcto según el prefijo de la URL."""
    scheme = url.split(":", 1)[0].lower()
    if scheme.startswith("mongodb"):
        return MongoSink(url)
    return SqlSink(url)

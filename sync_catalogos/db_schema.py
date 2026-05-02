"""Schema inference: infiere columnas SQL apropiadas a partir de samples reales.

Para cada catálogo se construye una tabla específica:
    salud_<catalog_name>
con columnas derivadas de las entradas (no una tabla genérica con `data JSON`).

Inferencia de tipo (heurística sobre values no-vacíos):
    - todos parsean como `int`            → BIGINT
    - todos parsean como `float`           → DOUBLE PRECISION
    - todos son SI/NO/Y/N/TRUE/FALSE/0/1   → BOOLEAN
    - todos son ISO date YYYY-MM-DD        → DATE
    - todos son fecha DD/MM/YYYY           → DATE
    - todos son fecha YYYYMMDD (8 dígitos) → DATE
    - resto: VARCHAR(N) ó TEXT según longitud máxima observada
        max <= 50  → VARCHAR(50)
        max <= 100 → VARCHAR(100)
        max <= 255 → VARCHAR(255)
        max <= 1000 → VARCHAR(1000)
        max > 1000 → TEXT

Sanitización de nombres de columna:
    - NFKD ASCII fold (María → Maria, álgido → algido, ñ → n)
    - Lowercase, snake_case
    - Reemplaza cualquier carácter no-[a-z0-9_] con `_`
    - Colapsa `_` repetidos, trim
    - Truncar a 63 chars (límite Postgres)
    - Prefijo `c_` si empieza con dígito
    - Dedup con sufijo `_2`, `_3`, ... si dos originales colapsan al mismo nombre
    - Renombra si choca con palabras reservadas SQL

Los VALORES de los datos preservan UTF-8 — no se sanea contenido, solo nombres
de tabla/columna que tienen restricciones del motor.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any


# ---------------------------------------------------------------------------
# Sanitization
# ---------------------------------------------------------------------------

# Subset suficiente para evitar conflictos en SQL/Postgres/MySQL/MSSQL
_RESERVED_SQL = frozenset({
    "select", "from", "where", "table", "group", "order", "by", "limit",
    "offset", "join", "left", "right", "inner", "outer", "on", "as",
    "and", "or", "not", "null", "true", "false", "is", "in", "like",
    "between", "exists", "all", "any", "case", "when", "then", "else",
    "end", "create", "drop", "alter", "insert", "update", "delete",
    "into", "values", "set", "primary", "key", "foreign", "references",
    "constraint", "default", "unique", "index", "view", "user", "grant",
    "revoke", "begin", "commit", "rollback", "transaction", "schema",
    "database", "column", "row", "level", "type", "to",
})


def ascii_fold(s: str) -> str:
    """Quita acentos y normaliza UTF-8 a ASCII básico."""
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def sanitize_identifier(name: str, *, max_length: int = 63) -> str:
    """Convierte cualquier string en un identificador SQL seguro."""
    s = ascii_fold(name).lower()
    # Reemplaza cualquier no-[a-z0-9_] por _
    s = re.sub(r"[^a-z0-9_]+", "_", s)
    # Colapsa _ repetidos y trim
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = "col"
    # Prefijo si empieza con dígito
    if s[0].isdigit():
        s = "c_" + s
    # Reserved word → suffix _
    if s in _RESERVED_SQL:
        s = s + "_"
    # Truncar
    if len(s) > max_length:
        s = s[:max_length].rstrip("_")
    return s


def dedupe_names(originals: list[str], *, max_length: int = 63) -> dict[str, str]:
    """Mapea cada original a un sql name único.

    Si dos originales colapsan al mismo sql name, se les añade sufijo _2, _3, ...
    """
    used: set[str] = set()
    out: dict[str, str] = {}
    for original in originals:
        base = sanitize_identifier(original, max_length=max_length)
        candidate = base
        i = 2
        while candidate in used:
            suffix = f"_{i}"
            candidate = (base[: max_length - len(suffix)] + suffix)
            i += 1
        used.add(candidate)
        out[original] = candidate
    return out


def sanitize_table_name(catalog_name: str, *, prefix: str = "salud_", max_length: int = 63) -> str:
    """Genera nombre de tabla seguro: prefix + catalog_name saneado."""
    base = sanitize_identifier(catalog_name, max_length=max_length - len(prefix))
    return prefix + base


# ---------------------------------------------------------------------------
# Type inference
# ---------------------------------------------------------------------------

@dataclass
class ColumnSpec:
    name: str            # nombre saneado para SQL
    original: str        # nombre original (key en el JSON / Mongo)
    sql_type_name: str   # "BIGINT" | "DOUBLE" | "BOOLEAN" | "DATE" | "VARCHAR(N)" | "TEXT"
    nullable: bool
    max_observed: int    # max length del string original (0 si no aplica)
    samples: int         # cuántos samples se evaluaron


_DATE_PATTERNS = [
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"),                  "%Y-%m-%d"),       # 2026-05-02
    (re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"), "iso"),            # ISO datetime (parse later)
    (re.compile(r"^\d{2}/\d{2}/\d{4}$"),                  "%d/%m/%Y"),       # 02/05/2026
    (re.compile(r"^\d{8}$"),                              "%Y%m%d"),         # 20260502
]
_BOOL_VALUES = frozenset({
    "si", "no", "sí", "true", "false", "y", "n", "yes", "0", "1", "t", "f",
})


def _is_int(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    if s[0] in "+-":
        s = s[1:]
    return s.isdigit() and len(s) <= 19  # cabe en BIGINT signed


def _is_float(s: str) -> bool:
    try:
        float(s.strip().replace(",", "."))  # tolera coma decimal latinoamericana
        return True
    except (ValueError, AttributeError):
        return False


def _is_date(s: str) -> bool:
    s = s.strip()
    return any(pat.match(s) for pat, _ in _DATE_PATTERNS)


def _is_bool(s: str) -> bool:
    return s.strip().lower() in _BOOL_VALUES


def _value_is_empty(v: Any) -> bool:
    return v is None or v == "" or (isinstance(v, str) and v.strip() == "")


def infer_column_type(
    values: list[Any],
    *,
    type_sample_size: int = 1000,
) -> tuple[str, int, bool]:
    """Devuelve (sql_type_name, max_observed, nullable) para una columna.

    - Para detección de tipo (int/float/bool/date) usa una muestra (sufuciente).
    - Para max_length usa TODOS los valores (preciso, evita truncar en bulk insert).
    """
    has_empty = any(_value_is_empty(v) for v in values)
    non_empty_all = [v for v in values if not _value_is_empty(v)]
    nullable = has_empty or not non_empty_all

    if not non_empty_all:
        return ("VARCHAR(50)", 0, True)

    # Sample para tipo
    type_sample = non_empty_all[:type_sample_size]
    str_sample = [str(v).strip() for v in type_sample]
    # Max length sobre TODOS los valores (no muestra)
    max_len = max(len(str(v).strip()) for v in non_empty_all)
    # Reasignar para usar abajo
    str_values = str_sample

    # Boolean: solo si todos los valores son booleanos típicos Y hay variedad
    # (evita marcar "1" → bool si en realidad es un código numérico)
    if all(_is_bool(s) for s in str_values):
        unique_lower = {s.lower() for s in str_values}
        # Solo bool si hay variedad de tokens (≥ 2 distintos) o si son los típicos SI/NO
        if unique_lower & {"si", "sí", "no"} or len(unique_lower) >= 2:
            if not all(_is_int(s) for s in str_values):
                return ("BOOLEAN", max_len, nullable)

    # Integer: todos parsean como int
    if all(_is_int(s) for s in str_values):
        # Excepción: si max_len > 10 dígitos, mejor BIGINT (igual ya asumimos BIGINT)
        # Pero si parece un código (lleva 0 al frente), preservar como string
        if any(s.startswith("0") and len(s) > 1 for s in str_values):
            return (_varchar(max_len), max_len, nullable)
        return ("BIGINT", max_len, nullable)

    # Float: todos parsean como float (incluye ints, así que el orden importa)
    if all(_is_float(s) for s in str_values):
        return ("DOUBLE PRECISION", max_len, nullable)

    # Date: todos coinciden con algún patrón de fecha
    if all(_is_date(s) for s in str_values):
        return ("DATE", max_len, nullable)

    # Default: VARCHAR / TEXT según longitud
    return (_varchar(max_len), max_len, nullable)


def _varchar(max_len: int) -> str:
    """Elige longitud con buffer de seguridad. Sube al siguiente bucket si
    el max está demasiado cerca del límite (evita romper si llegan valores
    nuevos un poco más largos en sync futuros).
    """
    # Buffer = max(8 chars, +25% del max)
    buffered = max_len + max(8, max_len // 4)
    if buffered <= 50:
        return "VARCHAR(50)"
    if buffered <= 100:
        return "VARCHAR(100)"
    if buffered <= 255:
        return "VARCHAR(255)"
    if buffered <= 1000:
        return "VARCHAR(1000)"
    if buffered <= 4000:
        return "VARCHAR(4000)"
    return "TEXT"


def infer_schema(entries: list[dict]) -> list[ColumnSpec]:
    """Infiere el schema completo de un catálogo desde sus entries."""
    if not entries:
        return []

    # Recolectar todas las keys, preservando orden de aparición
    all_keys: list[str] = []
    seen_keys: set[str] = set()
    for e in entries[:200]:
        if not isinstance(e, dict):
            continue
        for k in e.keys():
            if k not in seen_keys:
                seen_keys.add(k)
                all_keys.append(k)

    name_map = dedupe_names(all_keys)

    specs: list[ColumnSpec] = []
    for original in all_keys:
        sql_name = name_map[original]
        col_values = [e.get(original) for e in entries if isinstance(e, dict)]
        sql_type, max_len, _nullable_inferred = infer_column_type(col_values)
        # Siempre permitir NULL: los catálogos pueden tener filas con campos
        # faltantes o vacíos, y no queremos rechazar bulk inserts por NOT NULL.
        specs.append(ColumnSpec(
            name=sql_name,
            original=original,
            sql_type_name=sql_type,
            nullable=True,
            max_observed=max_len,
            samples=len(col_values),
        ))
    return specs


# ---------------------------------------------------------------------------
# Value coercion (string raw → tipo inferido)
# ---------------------------------------------------------------------------

def coerce_value(v: Any, sql_type: str) -> Any:
    """Transforma un valor del JSON al tipo inferido. None si vacío."""
    if _value_is_empty(v):
        return None
    s = str(v).strip()

    if sql_type == "BIGINT":
        try:
            return int(s)
        except ValueError:
            return None
    if sql_type == "DOUBLE PRECISION":
        try:
            return float(s.replace(",", "."))
        except ValueError:
            return None
    if sql_type == "BOOLEAN":
        return s.lower() in {"si", "sí", "true", "y", "yes", "1", "t"}
    if sql_type == "DATE":
        for pat, fmt in _DATE_PATTERNS:
            if pat.match(s):
                try:
                    if fmt == "iso":
                        return datetime.fromisoformat(s).date()
                    return datetime.strptime(s, fmt).date()
                except ValueError:
                    continue
        return None
    # VARCHAR/TEXT — preservar UTF-8 tal cual
    return s

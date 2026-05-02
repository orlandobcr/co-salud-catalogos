"""Lectura / escritura atómica de archivos JSON de catálogo."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path

from .schema import CatalogFile


def write_catalog(path: Path, catalog: CatalogFile) -> None:
    """Escribe el catálogo en `path` de forma atómica (tmpfile → rename)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = catalog.to_dict()
    body = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False)
    fd, tmp = tempfile.mkstemp(prefix=".tmp.", suffix=".json", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(body)
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def hash_entries(entries: list) -> str:
    body = json.dumps(entries, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()

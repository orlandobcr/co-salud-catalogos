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


class EntriesHasher:
    """Calcula el mismo sha256 que `hash_entries` sin materializar la lista.

    `hash_entries` serializa la lista completa con `sort_keys` y separadores
    compactos; eso equivale a "[" + ",".join(dumps(fila)) + "]". Alimentando el
    hash con esas mismas piezas se obtiene byte a byte el mismo digest, lo que
    permite comparar un catálogo escrito en streaming contra uno escrito de
    una sola vez.
    """

    def __init__(self) -> None:
        self._h = hashlib.sha256()
        self._h.update(b"[")
        self._empty = True
        self._count = 0

    def update(self, entry) -> None:
        chunk = json.dumps(entry, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        if not self._empty:
            self._h.update(b",")
        self._h.update(chunk.encode("utf-8"))
        self._empty = False
        self._count += 1

    def hexdigest(self) -> str:
        h = self._h.copy()
        h.update(b"]")
        return h.hexdigest()

    @property
    def count(self) -> int:
        return self._count

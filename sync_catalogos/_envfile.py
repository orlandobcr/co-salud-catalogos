"""Carga `.env` del cwd o de la raíz del paquete sin dependencia externa.

Soporta sintaxis básica: `KEY=value`, `KEY="value with spaces"`, comentarios
con `#`. NO ejecuta shell, NO interpola variables. Si la var ya existe en
`os.environ`, no se sobreescribe (el ambiente del SO siempre gana).
"""

from __future__ import annotations

import os
import re
from pathlib import Path

_LINE_RE = re.compile(r'^\s*(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<value>.*?)\s*$')


def load_env(path: Path | str | None = None) -> int:
    """Carga el .env. Devuelve cantidad de variables nuevas seteadas.

    Buscamos en orden:
        1. `path` argumento (si existe)
        2. `./.env` (cwd)
        3. `<package_root>/.env`
    """
    candidates: list[Path] = []
    if path is not None:
        candidates.append(Path(path))
    candidates.append(Path.cwd() / ".env")
    candidates.append(Path(__file__).resolve().parent.parent / ".env")

    target: Path | None = None
    for c in candidates:
        if c.exists() and c.is_file():
            target = c
            break
    if target is None:
        return 0

    n = 0
    for raw in target.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = _LINE_RE.match(line)
        if not m:
            continue
        key = m.group("key")
        value = m.group("value")
        # quitar comillas balanceadas
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        # SO siempre gana
        if key in os.environ:
            continue
        os.environ[key] = value
        n += 1
    return n

"""Cortes: capturas fechadas e inmutables del estado de los catálogos.

Un **corte** es el contenido de los 316 catálogos en un momento dado, guardado
en disco comprimido y acompañado de un manifest. Su razón de ser es poder
responder "¿qué cambió entre el 19 de septiembre y hoy?" — algo que hasta ahora
era imposible, porque cada sync sobrescribía al anterior sin dejar rastro.

Decisiones de diseño
--------------------

**Los cortes se exportan desde la base, no desde el sync.** Así el corte refleja
exactamente lo que sirve el API y no lo que se creyó descargar; esa divergencia
es justamente la que escondió el bug P0 de paginación durante meses. Además
permite cortar sin sincronizar.

**Incrementalidad por hash.** Si el `sha256` de un catálogo no cambió respecto
al corte anterior, no se reescribe el archivo: el manifest apunta al corte donde
sí está (`same_as`). Un corte donde nada cambió cuesta unos kilobytes.

Se guardan dos hashes por catálogo, y no son intercambiables:

- `source_sha256` — el que calculó el sync, tal como quedó en
  `salud_catalog_metadata`. Sirve de descarte barato: si no cambió, ni siquiera
  hace falta leer la tabla.
- `sha256` — el de las filas tal como salen de la base. No coincide con el
  anterior, porque al escribir se aplicó `coerce_value` (los vacíos se vuelven
  NULL, los strings se recortan). Es el que vale para comparar cortes entre sí,
  porque ambos lados pasaron por la misma transformación.

**Memoria acotada.** Se lee con cursor server-side y se escribe gzip a medida.
El server tiene 1 GB de RAM y `sispro_cups_gr_servicios` tiene 1,44 M de filas.

Layout::

    <root>/2026-09-19/manifest.json
    <root>/2026-09-19/co/clinical/cie10.json.gz
    <root>/2026-11-02/manifest.json            <- sólo los que cambiaron
"""

from __future__ import annotations

import gzip
import hashlib
import json
import logging
import os
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from .io import EntriesHasher
from .sources import REGISTRY

log = logging.getLogger(__name__)

MANIFEST = "manifest.json"
_READ_CHUNK = 1000


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _jsonable(v: Any) -> Any:
    """Los tipos que el driver devuelve y `json` no sabe serializar."""
    if isinstance(v, (datetime, date)):
        return v.isoformat()
    if isinstance(v, (bytes, bytearray)):
        return v.decode("utf-8", "replace")
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    return str(v)


def _output_path_for(name: str) -> Path:
    """Ruta relativa del catálogo dentro del corte, con el layout del repo."""
    for src in REGISTRY:
        if src.name == name:
            return src.output_path.with_suffix(".json.gz")
    return Path(f"{name}.json.gz")


# ---------------------------------------------------------------------------
# Lectura desde la base
# ---------------------------------------------------------------------------

@dataclass
class CatalogRef:
    name: str
    table_name: str
    row_count: int | None
    source_sha256: str | None
    metadata: dict[str, Any]
    columns: list[tuple[str, str]]   # (columna sql, clave original)


def read_catalog_refs(conn) -> list[CatalogRef]:
    """Lee el inventario de catálogos desde `salud_catalog_metadata`."""
    import sqlalchemy as sa

    rows = conn.execute(sa.text(
        "SELECT name, description, source, source_url, source_id, version, "
        "license, row_count, last_synced, sha256, notes, table_name, schema_json "
        "FROM salud_catalog_metadata ORDER BY name"
    )).mappings().all()

    refs: list[CatalogRef] = []
    for r in rows:
        schema = json.loads(r["schema_json"]) if r["schema_json"] else []
        cols = [(c["col"], c.get("from") or c["col"]) for c in schema]
        meta = {
            "name": r["name"],
            "description": r["description"],
            "source": r["source"],
            "source_url": r["source_url"],
            "source_id": r["source_id"],
            "version": r["version"],
            "license": r["license"],
            "row_count": r["row_count"],
            "last_synced": _jsonable(r["last_synced"]),
            "sha256": r["sha256"],
            "notes": r["notes"],
        }
        refs.append(CatalogRef(
            name=r["name"],
            table_name=r["table_name"] or "",
            row_count=r["row_count"],
            source_sha256=r["sha256"],
            metadata={k: v for k, v in meta.items() if v is not None},
            columns=cols,
        ))
    return refs


def iter_entries(conn, ref: CatalogRef) -> Iterator[dict[str, Any]]:
    """Emite las filas de un catálogo con cursor server-side (memoria constante)."""
    import sqlalchemy as sa

    if not ref.table_name or not ref.columns:
        return
    sel = ", ".join(f'"{c}"' for c, _ in ref.columns)
    stmt = sa.text(f'SELECT {sel} FROM "{ref.table_name}" ORDER BY "_idx"')
    result = conn.execution_options(
        stream_results=True, yield_per=_READ_CHUNK
    ).execute(stmt)
    keys = [orig for _, orig in ref.columns]
    for row in result:
        yield {k: _jsonable(v) for k, v in zip(keys, row)}


# ---------------------------------------------------------------------------
# Escritura de un catálogo dentro de un corte
# ---------------------------------------------------------------------------

def write_catalog_gz(path: Path, metadata: dict, entries: Iterator[dict]) -> tuple[int, str]:
    """Escribe `{metadata, entries}` comprimido, a medida que llegan las filas.

    Devuelve `(row_count, sha256)`. La escritura es atómica: se escribe a un
    temporal y se renombra, para que un corte nunca quede a medias.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    hasher = EntriesHasher()
    tmp = path.with_name(path.name + ".tmp")
    try:
        with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=6) as f:
            f.write('{"metadata":')
            json.dump(metadata, f, ensure_ascii=False)
            f.write(',"entries":[')
            primero = True
            for entry in entries:
                hasher.update(entry)
                if not primero:
                    f.write(",")
                f.write(json.dumps(entry, ensure_ascii=False, sort_keys=True,
                                   separators=(",", ":")))
                primero = False
            f.write("]}")
        os.replace(tmp, path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    return hasher.count, hasher.hexdigest()


def read_entries_gz(path: Path) -> Iterator[dict]:
    """Lee las entries de un `.json.gz` de corte. Carga el archivo entero."""
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return iter(json.load(f).get("entries") or [])


# ---------------------------------------------------------------------------
# Manifests
# ---------------------------------------------------------------------------

def listar_cortes(root: Path) -> list[str]:
    if not root.is_dir():
        return []
    return sorted(d.name for d in root.iterdir() if (d / MANIFEST).is_file())


def load_manifest(root: Path, corte_id: str) -> dict:
    p = root / corte_id / MANIFEST
    if not p.is_file():
        raise FileNotFoundError(f"no existe el corte {corte_id} en {root}")
    return json.loads(p.read_text(encoding="utf-8"))


def resolve_file(root: Path, corte_id: str, catalogo: str) -> Path:
    """Dónde viven realmente los datos, siguiendo la cadena de `same_as`."""
    visto: set[str] = set()
    actual = corte_id
    while actual not in visto:
        visto.add(actual)
        man = load_manifest(root, actual)
        ent = (man.get("catalogos") or {}).get(catalogo)
        if ent is None:
            raise KeyError(f"{catalogo} no está en el corte {actual}")
        if ent.get("file"):
            return root / actual / ent["file"]
        siguiente = ent.get("same_as")
        if not siguiente:
            raise KeyError(f"{catalogo} en {actual} no tiene datos ni same_as")
        actual = siguiente
    raise RuntimeError(f"ciclo de same_as resolviendo {catalogo} desde {corte_id}")


# ---------------------------------------------------------------------------
# Crear un corte
# ---------------------------------------------------------------------------

def crear_corte(
    engine,
    root: Path,
    corte_id: str,
    *,
    previous: str | None = None,
    notes: str = "",
    progress_cb=None,
) -> dict:
    """Exporta el estado actual de la base como un corte nuevo."""
    if (root / corte_id / MANIFEST).exists():
        raise FileExistsError(f"el corte {corte_id} ya existe — los cortes son inmutables")

    anteriores = listar_cortes(root)
    if previous is None and anteriores:
        previous = anteriores[-1]
    man_prev = load_manifest(root, previous) if previous else {"catalogos": {}}
    prev_cats = man_prev.get("catalogos") or {}

    catalogos: dict[str, dict] = {}
    reusados = escritos = 0
    with engine.connect() as conn:
        refs = read_catalog_refs(conn)
        for i, ref in enumerate(refs, 1):
            anterior = prev_cats.get(ref.name)
            # Descarte barato: si el sync no tocó el catálogo, no leemos la tabla.
            if (
                anterior is not None
                and ref.source_sha256 is not None
                and anterior.get("source_sha256") == ref.source_sha256
            ):
                catalogos[ref.name] = {
                    "row_count": anterior.get("row_count"),
                    "sha256": anterior.get("sha256"),
                    "source_sha256": ref.source_sha256,
                    "file": None,
                    "same_as": anterior.get("same_as") or previous,
                }
                reusados += 1
            else:
                rel = _output_path_for(ref.name)
                n, sha = write_catalog_gz(
                    root / corte_id / rel, ref.metadata, iter_entries(conn, ref)
                )
                catalogos[ref.name] = {
                    "row_count": n,
                    "sha256": sha,
                    "source_sha256": ref.source_sha256,
                    "file": str(rel),
                    "same_as": None,
                }
                escritos += 1
            if progress_cb is not None:
                progress_cb(i, len(refs), ref.name)

    manifest = {
        "corte_id": corte_id,
        "created_at": _now_iso(),
        "previous": previous,
        "notes": notes,
        "catalogos": catalogos,
    }
    (root / corte_id).mkdir(parents=True, exist_ok=True)
    (root / corte_id / MANIFEST).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    manifest["_escritos"] = escritos
    manifest["_reusados"] = reusados
    return manifest


# ---------------------------------------------------------------------------
# Libro en Postgres
# ---------------------------------------------------------------------------

def registrar_en_db(engine, manifest: dict) -> None:
    """Deja el índice del corte en `salud_cortes` para poder consultarlo en SQL."""
    import sqlalchemy as sa

    md = sa.MetaData()
    t = sa.Table(
        "salud_cortes", md,
        sa.Column("corte_id", sa.String(64), primary_key=True),
        sa.Column("catalogo", sa.String(200), primary_key=True),
        sa.Column("row_count", sa.BigInteger),
        sa.Column("sha256", sa.String(64)),
        sa.Column("source_sha256", sa.String(64)),
        sa.Column("same_as", sa.String(64)),
        sa.Column("created_at", sa.DateTime(timezone=True)),
    )
    md.create_all(engine)
    creado = datetime.fromisoformat(manifest["created_at"])
    filas = [
        {
            "corte_id": manifest["corte_id"], "catalogo": nombre,
            "row_count": d.get("row_count"), "sha256": d.get("sha256"),
            "source_sha256": d.get("source_sha256"), "same_as": d.get("same_as"),
            "created_at": creado,
        }
        for nombre, d in (manifest.get("catalogos") or {}).items()
    ]
    with engine.begin() as conn:
        conn.execute(sa.delete(t).where(t.c.corte_id == manifest["corte_id"]))
        if filas:
            conn.execute(sa.insert(t), filas)


# ---------------------------------------------------------------------------
# Diff
# ---------------------------------------------------------------------------

def _row_key(entry: dict) -> bytes:
    body = json.dumps(entry, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.blake2b(body.encode("utf-8"), digest_size=8).digest()


def diff_catalogo(root: Path, a: str, b: str, catalogo: str) -> dict:
    """Altas y bajas de un catálogo entre dos cortes.

    Identidad de fila = hash de la fila completa, así que una fila *modificada*
    cuenta como una baja más un alta. Distinguirlas requiere declarar columnas
    clave por catálogo, que todavía no está implementado.
    """
    try:
        fa = resolve_file(root, a, catalogo)
    except KeyError:
        fa = None
    try:
        fb = resolve_file(root, b, catalogo)
    except KeyError:
        fb = None

    if fa is None and fb is None:
        raise KeyError(f"{catalogo} no está en ninguno de los dos cortes")
    if fa is None:
        n = sum(1 for _ in read_entries_gz(fb))
        return {"catalogo": catalogo, "estado": "nuevo", "filas_a": 0, "filas_b": n,
                "altas": n, "bajas": 0}
    if fb is None:
        n = sum(1 for _ in read_entries_gz(fa))
        return {"catalogo": catalogo, "estado": "eliminado", "filas_a": n, "filas_b": 0,
                "altas": 0, "bajas": n}

    restantes: set[bytes] = set()
    filas_a = 0
    for e in read_entries_gz(fa):
        restantes.add(_row_key(e))
        filas_a += 1
    altas = filas_b = 0
    for e in read_entries_gz(fb):
        filas_b += 1
        k = _row_key(e)
        if k in restantes:
            restantes.discard(k)
        else:
            altas += 1
    return {
        "catalogo": catalogo, "estado": "igual" if not altas and not restantes else "cambiado",
        "filas_a": filas_a, "filas_b": filas_b, "altas": altas, "bajas": len(restantes),
    }


def diff_cortes(root: Path, a: str, b: str, *, catalogo: str | None = None) -> list[dict]:
    ma, mb = load_manifest(root, a), load_manifest(root, b)
    nombres = sorted(set(ma.get("catalogos") or {}) | set(mb.get("catalogos") or {}))
    if catalogo:
        if catalogo not in nombres:
            raise KeyError(f"{catalogo} no está en ninguno de los dos cortes")
        nombres = [catalogo]
    salida = []
    for n in nombres:
        ca = (ma.get("catalogos") or {}).get(n)
        cb = (mb.get("catalogos") or {}).get(n)
        # Atajo: mismo hash de contenido ⇒ idénticos, sin abrir los archivos.
        if ca and cb and ca.get("sha256") and ca["sha256"] == cb.get("sha256"):
            salida.append({"catalogo": n, "estado": "igual",
                           "filas_a": ca.get("row_count"), "filas_b": cb.get("row_count"),
                           "altas": 0, "bajas": 0})
            continue
        salida.append(diff_catalogo(root, a, b, n))
    return salida


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(
        prog="python -m sync_catalogos.cortes",
        description="Cortes: capturas fechadas e inmutables de los catálogos.",
    )
    ap.add_argument("--root", default=os.environ.get("SALUD_CORTES_ROOT", "./cortes"),
                    help="directorio raíz de los cortes (env SALUD_CORTES_ROOT)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_crear = sub.add_parser("crear", help="exporta el estado actual de la base")
    p_crear.add_argument("--id", help="id del corte (default: fecha de hoy)")
    p_crear.add_argument("--db", required=True, help="URL SQLAlchemy de la base")
    p_crear.add_argument("--previous", help="corte anterior (default: el último)")
    p_crear.add_argument("--notes", default="", help="nota libre para el manifest")
    p_crear.add_argument("--no-registrar", action="store_true",
                         help="no escribir el índice en la tabla salud_cortes")

    sub.add_parser("listar", help="lista los cortes existentes")

    p_diff = sub.add_parser("diff", help="altas y bajas entre dos cortes")
    p_diff.add_argument("a")
    p_diff.add_argument("b")
    p_diff.add_argument("--catalogo")
    p_diff.add_argument("--json", action="store_true")

    p_ext = sub.add_parser("extraer", help="vuelca un catálogo de un corte")
    p_ext.add_argument("corte")
    p_ext.add_argument("--catalogo", required=True)
    p_ext.add_argument("--out", help="archivo destino (default: stdout)")

    args = ap.parse_args(argv)
    root = Path(args.root).expanduser()

    if args.cmd == "listar":
        cortes = listar_cortes(root)
        if not cortes:
            print(f"no hay cortes en {root}")
            return 0
        for c in cortes:
            m = load_manifest(root, c)
            cats = m.get("catalogos") or {}
            propios = sum(1 for d in cats.values() if d.get("file"))
            filas = sum(d.get("row_count") or 0 for d in cats.values())
            print(f"{c}  {len(cats):>4} catálogos  {filas:>12,} filas  "
                  f"{propios:>4} archivos propios  {m.get('created_at','')}")
        return 0

    if args.cmd == "crear":
        import sqlalchemy as sa
        corte_id = args.id or datetime.now(timezone.utc).strftime("%Y-%m-%d")
        engine = sa.create_engine(args.db)

        def _prog(i, total, nombre):
            print(f"\r  [{i}/{total}] {nombre[:44]:44s}", end="", flush=True)

        man = crear_corte(engine, root, corte_id, previous=args.previous,
                          notes=args.notes, progress_cb=_prog)
        print()
        if not args.no_registrar:
            registrar_en_db(engine, man)
        cats = man["catalogos"]
        filas = sum(d.get("row_count") or 0 for d in cats.values())
        tam = sum(f.stat().st_size for f in (root / corte_id).rglob("*.json.gz"))
        print(f"corte {corte_id}: {len(cats)} catálogos, {filas:,} filas")
        print(f"  escritos: {man['_escritos']}   reusados del corte anterior: {man['_reusados']}")
        print(f"  tamaño en disco: {tam/1e6:.1f} MB   anterior: {man.get('previous') or '—'}")
        return 0

    if args.cmd == "diff":
        filas = diff_cortes(root, args.a, args.b, catalogo=args.catalogo)
        if args.json:
            print(json.dumps(filas, ensure_ascii=False, indent=2))
            return 0
        cambiados = [f for f in filas if f["estado"] != "igual"]
        print(f"{'catálogo':44}{'A':>11}{'B':>11}{'altas':>10}{'bajas':>10}")
        print("-" * 86)
        for f in cambiados:
            print(f"{f['catalogo']:44}{f['filas_a'] or 0:>11,}{f['filas_b'] or 0:>11,}"
                  f"{f['altas']:>10,}{f['bajas']:>10,}")
        print("-" * 86)
        print(f"{len(cambiados)} catálogos cambiados de {len(filas)}   "
              f"altas {sum(f['altas'] for f in filas):,}   "
              f"bajas {sum(f['bajas'] for f in filas):,}")
        return 0

    if args.cmd == "extraer":
        p = resolve_file(root, args.corte, args.catalogo)
        datos = gzip.open(p, "rt", encoding="utf-8").read()
        if args.out:
            Path(args.out).write_text(datos, encoding="utf-8")
            print(f"{args.catalogo} de {args.corte} → {args.out}")
        else:
            print(datos)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())

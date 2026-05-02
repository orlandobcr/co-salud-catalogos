"""CLI sync entry point.

Uso:
    python -m sync_catalogos.sync --list
    python -m sync_catalogos.sync --catalog divipola_municipios
    python -m sync_catalogos.sync --all
    python -m sync_catalogos.sync --all --kind socrata
    python -m sync_catalogos.sync --all --kind reps_export
    python -m sync_catalogos.sync --all --kind sispro_aspx --i-have-permission
    python -m sync_catalogos.sync --all --dry-run

Output:
    catalogos_co/co/<area>/<name>.json   (escritura atómica)

Exit code 0 si todo OK, !=0 si hubo algún error. Compatible con cron.

Variable de entorno:
    SALUD_CATALOGS_ROOT  — directorio destino (default: ./catalogos_co)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

from . import reps, sispro, socrata
from .io import hash_entries, write_catalog
from .schema import CatalogFile, CatalogMetadata
from .sources import REGISTRY, CatalogSource, find


def catalogs_root() -> Path:
    """Directorio raíz para los JSONs sincronizados."""
    env = os.environ.get("SALUD_CATALOGS_ROOT", "").strip()
    if env:
        return Path(env).expanduser().resolve()
    # Default: hermano del paquete (proyecto/catalogos_co)
    here = Path(__file__).resolve().parent.parent
    return here / "catalogos_co"


def _now_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _source_url(src: CatalogSource) -> str:
    if src.kind == "socrata" and src.socrata_dataset_id:
        return f"https://www.datos.gov.co/resource/{src.socrata_dataset_id}.json"
    if src.kind == "sispro_aspx" and src.sispro_code:
        return f"{sispro.SISPRO_BASE}{sispro.SISPRO_PATH}?Code={src.sispro_code}"
    if src.kind == "reps_export" and src.reps_endpoint:
        return reps.endpoint_url(src.reps_endpoint)
    return src.manual_source_url


def _build_metadata(src: CatalogSource, entries: list, version: str | None) -> CatalogMetadata:
    return CatalogMetadata(
        name=src.name,
        description=src.description,
        source=src.kind,
        source_url=_source_url(src),
        source_id=(src.socrata_dataset_id or src.sispro_code or src.reps_endpoint or None),
        version=version,
        license=src.license,
        row_count=len(entries),
        last_synced=_now_iso(),
        sha256=hash_entries(entries),
        notes=src.notes,
    )


def sync_one(
    src: CatalogSource,
    *,
    dry_run: bool = False,
    verbose: bool = True,
    consent: bool = False,
) -> dict:
    """Sincroniza un solo catálogo. Devuelve un dict de resultado para el CLI."""
    out_path = catalogs_root() / src.output_path
    started = time.perf_counter()

    if src.kind == "manual":
        return {
            "name": src.name,
            "kind": "manual",
            "skipped": True,
            "reason": "catálogo manual — no se sincroniza desde remoto",
            "path": str(out_path),
        }

    if src.requires_explicit_consent and not consent:
        return {
            "name": src.name,
            "kind": src.kind,
            "skipped": True,
            "reason": "requiere flag --i-have-permission (ver consent_reason)",
            "consent_reason": src.consent_reason,
            "path": str(out_path),
        }

    def _progress(n):
        if verbose:
            sys.stdout.write(f"\r  [{src.name}] {n} filas...")
            sys.stdout.flush()

    try:
        if src.kind == "socrata":
            assert src.socrata_dataset_id
            entries = socrata.fetch_all(
                src.socrata_dataset_id,
                where=src.socrata_extra_query,
                progress_cb=_progress if verbose else None,
            )
            version = socrata.remote_version(src.socrata_dataset_id)
        elif src.kind == "sispro_aspx":
            assert src.sispro_code
            entries, _total = sispro.fetch_all(
                src.sispro_code,
                page_size=src.sispro_page_size,
                progress_cb=_progress if verbose else None,
            )
            version = _now_iso()
        elif src.kind == "reps_export":
            assert src.reps_endpoint
            entries = reps.fetch_export(
                src.reps_endpoint,
                progress_cb=_progress if verbose else None,
            )
            version = _now_iso()
        else:
            return {"name": src.name, "skipped": True, "reason": f"kind desconocido {src.kind}"}
    except Exception as e:
        if verbose:
            sys.stdout.write("\n")
        return {
            "name": src.name,
            "error": str(e),
            "duration_s": round(time.perf_counter() - started, 2),
        }

    if verbose:
        sys.stdout.write("\n")

    metadata = _build_metadata(src, entries, version)
    catalog = CatalogFile(metadata=metadata, entries=entries)

    if dry_run:
        return {
            "name": src.name,
            "kind": src.kind,
            "rows": len(entries),
            "dry_run": True,
            "path": str(out_path),
            "duration_s": round(time.perf_counter() - started, 2),
        }

    write_catalog(out_path, catalog)
    return {
        "name": src.name,
        "kind": src.kind,
        "rows": len(entries),
        "path": str(out_path),
        "version": version,
        "sha256_short": (metadata.sha256 or "")[:12],
        "duration_s": round(time.perf_counter() - started, 2),
    }


def sync_all(*, kind: str | None = None, dry_run: bool = False, consent: bool = False) -> list[dict]:
    results: list[dict] = []
    for src in REGISTRY:
        if kind is not None and src.kind != kind:
            continue
        if src.kind == "manual":
            continue
        results.append(sync_one(src, dry_run=dry_run, consent=consent))
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--catalog", help="nombre de un solo catálogo (ver REGISTRY)")
    g.add_argument("--all", action="store_true", help="sincroniza todos los no-manuales")
    g.add_argument("--list", action="store_true", help="lista catálogos registrados y sale")
    ap.add_argument(
        "--kind",
        choices=["socrata", "sispro_aspx", "reps_export"],
        help="filtra por tipo de fuente (con --all)",
    )
    ap.add_argument("--dry-run", action="store_true", help="no escribe archivos")
    ap.add_argument("--json", action="store_true", help="emite resumen JSON")
    ap.add_argument(
        "--i-have-permission",
        dest="consent",
        action="store_true",
        help=(
            "ack consent para fuentes con robots.txt restrictivo (ej. SISPRO). "
            "Solo para corridas manuales documentadas — nunca en cron."
        ),
    )
    args = ap.parse_args(argv)

    if args.list:
        print(f"  {'NAME':30s}  {'KIND':13s}  {'SOURCE_ID':30s}  PATH")
        print("  " + "-" * 110)
        for s in REGISTRY:
            extra = s.socrata_dataset_id or s.sispro_code or s.reps_endpoint or ""
            print(f"  {s.name:30s}  {s.kind:13s}  {extra:30s}  {s.output_path}")
        return 0

    if args.catalog:
        src = find(args.catalog)
        if src is None:
            print(f"catálogo desconocido: {args.catalog}", file=sys.stderr)
            return 2
        result = sync_one(src, dry_run=args.dry_run, consent=args.consent)
        results = [result]
    else:
        results = sync_all(kind=args.kind, dry_run=args.dry_run, consent=args.consent)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        ok = [r for r in results if "error" not in r and not r.get("skipped")]
        bad = [r for r in results if "error" in r]
        skip = [r for r in results if r.get("skipped")]
        print()
        print(f"Sincronizados: {len(ok)}  con error: {len(bad)}  saltados: {len(skip)}")
        for r in ok:
            print(f"  ✓ {r['name']:28s}  {r.get('rows', '-'):>8}  {r.get('duration_s', '-')}s  → {r.get('path')}")
        for r in bad:
            print(f"  ✗ {r['name']:28s}  ERROR: {r['error']}")
        for r in skip:
            print(f"  · {r['name']:28s}  skip: {r['reason']}")

    return 0 if all("error" not in r for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

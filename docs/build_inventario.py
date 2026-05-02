"""Genera docs/inventario_fuentes.md a partir de los JSON sincronizados.

Uso:
    cd cac-salud-catalogos
    python docs/build_inventario.py > docs/inventario_fuentes.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "catalogos_co" / "co"
AREAS = {
    "institutional": "Institucional (REPS, EAPB, IPS, redes)",
    "clinical":      "Clínico (diagnósticos, procedimientos, medicamentos, vacunas, enfermedades)",
    "rips":          "RIPS — auditoría / validación de reportes",
    "financial":     "Financiero (recobros, PILA, ARL, CCF, pagos, subsidios)",
    "admin":         "Administrativo / demografía (tipos de ID, sexo, ocupación, régimen, afiliación)",
    "geo":           "Geografía (DIVIPOLA, postales, vías, países)",
    "misc":          "Misceláneos (demás tablas SISPRO sin categoría específica)",
}


def fmt_size(n: float) -> str:
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def main() -> int:
    out: list[str] = []

    def w(s: str = "") -> None:
        out.append(s)

    w("# Inventario de fuentes y esquemas")
    w("")
    w("Generado a partir de los catálogos sincronizados en `catalogos_co/co/`.")
    w("Cada catálogo trae metadata reproducible (URL fuente, versión, sha256, fecha de sync).")
    w("")
    w("**Cómo regenerar este inventario:**")
    w("```bash")
    w("python docs/build_inventario.py > docs/inventario_fuentes.md")
    w("```")
    w("")
    w("---")
    w("")

    all_files: list[tuple[str, Path]] = []
    for area in AREAS:
        for f in sorted((ROOT / area).glob("*.json")):
            all_files.append((area, f))

    # Tabla resumen
    w("## Resumen")
    w("")
    w("| Catálogo | Kind | Filas | Tamaño | URL fuente |")
    w("|----------|------|------:|-------:|------------|")
    for _area, f in all_files:
        cat = json.loads(f.read_text(encoding="utf-8"))
        meta = cat.get("metadata", {})
        rc = meta.get("row_count") or len(cat.get("entries", []))
        sz = fmt_size(f.stat().st_size)
        url = meta.get("source_url", "")
        w(f"| `{meta.get('name', f.stem)}` | `{meta.get('source','?')}` | {rc:,} | {sz} | <{url}> |")
    w("")
    w("---")
    w("")

    total_rows = 0
    total_bytes = 0

    for area, area_label in AREAS.items():
        files = sorted((ROOT / area).glob("*.json"))
        if not files:
            continue
        w(f"## {area_label}")
        w("")
        for f in files:
            size = f.stat().st_size
            total_bytes += size
            cat = json.loads(f.read_text(encoding="utf-8"))
            meta = cat.get("metadata", {}) or {}
            entries = cat.get("entries", []) or []
            total_rows += len(entries)

            cols = list(entries[0].keys()) if entries and isinstance(entries[0], dict) else []
            name = meta.get("name", f.stem)
            kind = meta.get("source", "?")
            url = meta.get("source_url", "")
            lic = meta.get("license", "")
            ver = meta.get("version", "?")
            rc = meta.get("row_count", len(entries))
            sha = (meta.get("sha256") or "")[:12]

            w(f"### `{name}`  ·  {rc:,} filas  ·  {fmt_size(size)}")
            w("")
            w(f"- **Kind**: `{kind}`")
            w(f"- **URL**: <{url}>")
            w(f"- **Licencia**: {lic}")
            w(f"- **Versión / sync**: {ver}  ·  sha256 `{sha}…`")
            if meta.get("notes"):
                w(f"- **Notas**: {meta['notes']}")
            w(f"- **Columnas** ({len(cols)}):")
            if cols:
                for i in range(0, len(cols), 6):
                    chunk = cols[i:i + 6]
                    w("  " + ", ".join(f"`{c}`" for c in chunk))
            if entries and isinstance(entries[0], dict):
                w("- **Ejemplo (fila 0, primeros 5 campos)**:")
                for k, v in list(entries[0].items())[:5]:
                    vs = str(v)
                    if len(vs) > 80:
                        vs = vs[:77] + "…"
                    w(f"  - `{k}`: `{vs}`")
            w("")
        w("")

    w("---")
    w("")
    w("## Totales")
    w("")
    w(f"- **{len(all_files)} catálogos**")
    w(f"- **{total_rows:,} filas** sincronizadas")
    w(f"- **{fmt_size(total_bytes)}** total en disco")

    sys.stdout.write("\n".join(out) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# co-salud-catalogos

Sincronización reproducible de los **catálogos públicos del sector salud en Colombia** — REPS Habilitación, SISPRO (tablas de referencia MinSalud) y Datos Abiertos Colombia.

Cada catálogo se descarga desde su fuente oficial y se guarda como JSON con metadata reproducible (URL fuente, versión, sha256, fecha de sync).

## Qué incluye

| Área           | Catálogos                                                              | Filas aprox |
|----------------|------------------------------------------------------------------------|-------------|
| Institucional  | REPS prestadores, sedes, servicios, capacidades, medidas, sanciones, EAPB, IPS por nivel, redes | 540k+ |
| Geografía      | DIVIPOLA dpto/mpio/centro poblado, códigos postales, vías INVIAS, países | 13k+        |
| Clínico        | CIE-10, CUPS, IUM, CUM INVIMA, ATC WHO, PBS, glosario, enfermedad huérfana, vacunación PAI/COVID | 67k+ |
| RIPS           | UNIRS, finalidad consulta, estado evolución, mapeo CUPS↔CIE↔servicios   | —           |
| Financiero     | Recobros, PILA, ARL, CCF, glosas, pagos, subsidios                     | —           |
| Administrativo | Tipos de identificación, sexo, ocupación, régimen, afiliación, nivel educativo | —     |

Total inicial: **319 catálogos · ~2.5M filas · ~3 GB en disco**.

Detalle completo y esquema de columnas de cada catálogo: [docs/inventario_fuentes.md](docs/inventario_fuentes.md).

## Fuentes y permisos

| Fuente | URL | robots.txt | Acceso |
|--------|-----|------------|--------|
| Datos Abiertos Colombia (Socrata) | `www.datos.gov.co/resource/{id}.json` | abierto | público, app token opcional |
| MinSalud SISPRO (ASPX) | `web.sispro.gov.co/WebPublico/Consultas/...` | `Disallow: /` | **el operador es responsable de obtener su propio permiso operativo** — ver [docs/permisos.md](docs/permisos.md) |
| MinSalud REPS Habilitación | `prestadores.minsalud.gov.co/habilitacion/consultas/*.aspx` | sin restricción | login `invitado/invitado` (público por diseño) |

## Instalación

```bash
uv venv
uv pip install -e .
```

O sin instalar (one-shot):
```bash
uv run --with httpx --with lxml python -m sync_catalogos.sync --list
```

## Uso

Listar todos los catálogos registrados:
```bash
python -m sync_catalogos.sync --list
```

Sincronizar uno solo:
```bash
python -m sync_catalogos.sync --catalog divipola_municipios
python -m sync_catalogos.sync --catalog reps_sedes
```

Sincronizar todos los abiertos (sin SISPRO):
```bash
python -m sync_catalogos.sync --all --kind socrata
python -m sync_catalogos.sync --all --kind reps_export
```

Sincronizar SISPRO (requiere consentimiento operativo documentado):
```bash
python -m sync_catalogos.sync --all --kind sispro_aspx --i-have-permission
```

Modo dry-run (no escribe archivos, solo cuenta filas):
```bash
python -m sync_catalogos.sync --all --dry-run
```

Salida JSON estructurada (para pipelines):
```bash
python -m sync_catalogos.sync --all --json > sync_report.json
```

## Variables de entorno

- `SALUD_SOCRATA_APP_TOKEN` — opcional, sube rate limit Socrata de ~1k/h a ~100k/h
- `SALUD_CATALOGS_ROOT` — directorio destino (default: `./catalogos_co`)

## Estructura de salida

```
catalogos_co/co/
├── institutional/      REPS (6 endpoints), EAPB, IPS, redes
├── clinical/           CIE-10, CUPS, IUM, CUM, ATC, PBS, vacunas, enfermedades
├── rips/               Validación / decodificación RIPS
├── financial/          Recobros, PILA, ARL, CCF, glosas, pagos
├── admin/              Tipos de ID, sexo, régimen, afiliación, demografía
├── geo/                DIVIPOLA, postales, vías, países
└── misc/               Demás tablas SISPRO sin categoría específica
```

Cada JSON tiene la forma:
```json
{
  "metadata": {
    "name": "reps_sedes",
    "description": "...",
    "source": "reps_export",
    "source_url": "https://prestadores.minsalud.gov.co/habilitacion/consultas/sedes_reps.aspx",
    "version": "2026-05-02T20:22:00Z",
    "license": "MinSalud REPS — Registro Especial de Prestadores (consulta pública)",
    "row_count": 76561,
    "last_synced": "2026-05-02T20:22:00Z",
    "sha256": "ef9e2ced00ff..."
  },
  "entries": [
    {"departamento": "...", "municipio": "...", ...}
  ]
}
```

## Cron / programación

- **REPS** (semanal — los datos cambian cuando se habilitan/dan de baja prestadores)
- **DIVIPOLA, códigos postales** (trimestral)
- **CIE-10, CUPS, IUM** (anual — actualizaciones formales del MinSalud)
- **SISPRO** — NUNCA en cron automático. El operador debe documentar cada ejecución (ver `docs/permisos.md`).

Ejemplo crontab (Socrata + REPS, sin SISPRO):
```cron
# Lunes 03:00 — sincronización semanal
0 3 * * 1 cd /opt/co-salud-catalogos && /usr/local/bin/uv run python -m sync_catalogos.sync --all --kind socrata >> /var/log/salud-sync.log 2>&1
30 3 * * 1 cd /opt/co-salud-catalogos && /usr/local/bin/uv run python -m sync_catalogos.sync --all --kind reps_export >> /var/log/salud-sync.log 2>&1
```

## Regenerar el inventario

Después de un sync, regenerar el inventario de esquemas:
```bash
python docs/build_inventario.py > docs/inventario_fuentes.md
```

## Licencias de los datos

- **Socrata datos.gov.co**: Datos Abiertos Colombia, Ley 1712/2014
- **REPS Habilitación**: consulta pública del Ministerio de Salud
- **SISPRO**: uso público sujeto a permiso operativo del MinSalud (responsabilidad del operador)

El **código** de este repo se distribuye bajo MIT. Los **datos** sincronizados conservan la licencia de su fuente original.

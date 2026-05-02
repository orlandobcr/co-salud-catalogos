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

## Documentación

| Doc | Audiencia | Para qué |
|-----|-----------|----------|
| [01 — Introducción gerencial](docs/01-introduccion-gerencial.md) | Decisión / dirección | Valor, casos de uso, costos, ROI |
| [02 — Arquitectura](docs/02-arquitectura.md) | Arquitectos / leads | Componentes, decisiones de diseño, modelo de datos |
| [03 — Funcionamiento](docs/03-funcionamiento.md) | Operadores / leads | Flujos por kind, idempotencia, scheduling, observabilidad |
| [04 — Manual de uso](docs/04-manual-uso.md) | Usuarios CLI | Comandos paso a paso, ejemplos, troubleshooting |
| [05 — Deep technical](docs/05-deep-technical.md) | Devs que extienden | Internals, cómo añadir source/sink/provider |
| [06 — Despliegue](docs/06-despliegue.md) | DevOps / SRE | Cron, Docker, K8s, sizing, hardening |
| [07 — Pruebas](docs/07-pruebas.md) | QA / DevOps | Smoke tests, validación pre-prod, CI |
| [08 — API REST + Dashboard](docs/08-api.md) | Integradores / consumidores | Auth Bearer JWT, permisos por catálogo, OpenAPI dinámico, dashboard web |
| [Inventario de fuentes](docs/inventario_fuentes.md) | Analistas | Esquema de columnas + ejemplo por catálogo |
| [Permisos](docs/permisos.md) | Compliance / legal | Régimen legal de cada fuente |
| [Proxy](docs/proxy.md) | DevOps | Pool de proxies opcional, providers, fallback |

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

## Persistencia opcional en DB (Postgres / MySQL / MSSQL / Mongo / SQLite)

Por defecto los catálogos se escriben como archivos JSON. Adicionalmente o en lugar de eso, se pueden escribir a una base de datos:

```bash
# Escribir a Postgres además de JSON
python -m sync_catalogos.sync --all --db "postgresql+psycopg://user:pass@host:5432/salud"

# Escribir solo a MySQL (sin JSON en disco)
python -m sync_catalogos.sync --all --db "mysql+pymysql://user:pass@host:3306/salud" --no-write-json

# MSSQL
python -m sync_catalogos.sync --all --db "mssql+pyodbc://user:pass@host/salud?driver=ODBC+Driver+18+for+SQL+Server"

# MongoDB
python -m sync_catalogos.sync --all --db "mongodb://user:pass@host:27017/salud"

# SQLite (gratis, sin server)
python -m sync_catalogos.sync --all --db "sqlite:///./salud.db"
```

Instalar el driver requerido:

```bash
uv pip install -e ".[db]"        # solo SQLAlchemy (suficiente para SQLite)
uv pip install -e ".[postgres]"  # SQLAlchemy + psycopg
uv pip install -e ".[mysql]"     # SQLAlchemy + pymysql
uv pip install -e ".[mssql]"     # SQLAlchemy + pyodbc
uv pip install -e ".[mongo]"     # pymongo
```

**Esquema (tipado, paridad SQL ↔ Mongo):**

Una tabla / colección **por cada catálogo**, con columnas inferidas desde los datos reales (no genérico con `data JSON`):

| Tabla / Collection | Contenido |
|--------------------|-----------|
| `salud_catalog_metadata` | 1 fila/doc por catálogo: `name, source, source_url, version, license, row_count, last_synced, sha256, notes, table_name, schema_json` |
| `salud_<catalog_name>` | N filas/docs por entry. Columnas tipadas según los datos: `_idx INTEGER PK`, `<col> <tipo>` |

**Inferencia de tipos** (sobre los datos reales):
- `BIGINT` — todos parsean como entero
- `DOUBLE PRECISION` — todos como float
- `BOOLEAN` — todos `SI/NO/Y/N/TRUE/FALSE`
- `DATE` — todos `YYYY-MM-DD`, `DD/MM/YYYY`, `YYYYMMDD`, o ISO datetime
- `VARCHAR(50/100/255/1000/4000)` o `TEXT` — según longitud máxima observada (con buffer de 25%)

**Sanitización de nombres** (acentos / caracteres especiales):
- `Municipio PNSR antes 2023` → `municipio_pnsr_antes_2023`
- `Extra_I:TipoRegimen` → `extra_i_tiporegimen`
- `Categorías Médicas` → `categorias_medicas` (acentos eliminados)
- ASCII fold + lowercase + snake_case + trunc a 63 chars + dedup con sufijo `_2`

**Los valores siempre preservan UTF-8** (`MEDELLÍN`, `ARCHIPIÉLAGO`, etc.) — solo los nombres de tabla/columna se sanean.

Estrategia de upsert: por catálogo, `DELETE + INSERT bulk` atómico. Idempotente.

## Variables de entorno

- `SALUD_SOCRATA_APP_TOKEN` — opcional, sube rate limit Socrata de ~1k/h a ~100k/h
- `SALUD_CATALOGS_ROOT` — directorio destino de los JSON (default: `./catalogos_co`)
- `TWOCAPTCHA_API_KEY` — opcional, activa el pool de proxies (ver `docs/proxy.md`)
- `PROXY_ENABLED` — `true` | `false` (default `false`)

Ver `.env.example` para la lista completa.

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

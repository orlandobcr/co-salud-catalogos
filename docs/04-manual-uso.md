# 4. Manual de uso

## Quickstart (3 minutos)

```bash
git clone https://github.com/orlandobcr/co-salud-catalogos
cd co-salud-catalogos
uv venv
uv pip install -e .

# Listar los 319 catálogos registrados
uv run python -m sync_catalogos.sync --list

# Sincronizar un catálogo pequeño para validar
uv run python -m sync_catalogos.sync --catalog divipola_departamentos

# Resultado:
# Sincronizados: 1  con error: 0  saltados: 0
#   ✓ divipola_departamentos        33  1.0s  → catalogos_co/co/geo/divipola_departamentos.json
```

Listo. Ahora puedes:
- correr `--all` para sincronizar todo lo abierto (Socrata + REPS),
- añadir `--db <url>` para persistir también a tu DB,
- añadir `--i-have-permission` para incluir los catálogos SISPRO,
- ver más opciones con `--help`.

---

## CLI completo

### Comandos principales

| Comando                                       | Uso                                                                |
|-----------------------------------------------|--------------------------------------------------------------------|
| `python -m sync_catalogos.sync --list`        | Lista los 319 catálogos registrados                                |
| `python -m sync_catalogos.sync --catalog X`   | Sincroniza un solo catálogo                                        |
| `python -m sync_catalogos.sync --all`         | Sincroniza todos los no-manuales (excepto los que necesitan consent)|
| `python -m sync_catalogos.proxy_check`        | Diagnóstico del pool de proxies                                    |
| `python docs/build_inventario.py > docs/inventario_fuentes.md` | Regenera el inventario tras un sync          |

### Modificadores de `sync`

| Flag                              | Default        | Descripción                                                |
|-----------------------------------|----------------|------------------------------------------------------------|
| `--kind {socrata, sispro_aspx, reps_export}` | (todos) | Filtra por tipo de fuente con `--all`                      |
| `--dry-run`                       | off            | No escribe archivos. Solo cuenta y reporta                |
| `--json`                          | off            | Output JSON estructurado                                   |
| `--i-have-permission`             | off            | Activa fuentes con `requires_explicit_consent=True` (SISPRO) |
| `--db <url>`                      | (sin DB)       | Persiste también a una DB (URL SQLAlchemy o `mongodb://`)  |
| `--no-write-json`                 | off            | No escribe los JSON en disco. Requiere `--db`              |

---

## Casos de uso

### 1. Solo lo que NO requiere consentimiento (cron seguro)

```bash
# Datos Abiertos (Socrata)
python -m sync_catalogos.sync --all --kind socrata

# REPS Habilitación
python -m sync_catalogos.sync --all --kind reps_export

# Ambos
python -m sync_catalogos.sync --all
# (los que requieren consent quedan automáticamente marcados como skipped)
```

### 2. Sincronizar SISPRO (con consentimiento operativo documentado)

```bash
# Catálogo individual
python -m sync_catalogos.sync --catalog cie10 --i-have-permission

# Todo SISPRO de una
python -m sync_catalogos.sync --all --kind sispro_aspx --i-have-permission
```

**Importante**: el flag `--i-have-permission` declara que el operador tiene autorización para acceder a SISPRO (cuyo `robots.txt` tiene `Disallow: /`). Cada ejecución debe quedar documentada en bitácora interna. NO debe automatizarse en cron.

Ver [permisos.md](permisos.md) para detalles legales.

### 3. Persistencia en base de datos (sin perder los JSON)

```bash
# A Postgres (escribe JSON Y a Postgres)
python -m sync_catalogos.sync --all \
    --db "postgresql+psycopg://user:pass@host:5432/salud"

# A MySQL
python -m sync_catalogos.sync --all \
    --db "mysql+pymysql://user:pass@host:3306/salud"

# A SQL Server
python -m sync_catalogos.sync --all \
    --db "mssql+pyodbc://user:pass@host/salud?driver=ODBC+Driver+18+for+SQL+Server"

# A MongoDB
python -m sync_catalogos.sync --all \
    --db "mongodb://user:pass@host:27017/salud"

# A SQLite local (cero infra)
python -m sync_catalogos.sync --all \
    --db "sqlite:///./salud_catalogos.db"
```

### 4. Solo a la DB, sin tocar disco

```bash
python -m sync_catalogos.sync --all \
    --db "postgresql+psycopg://..." \
    --no-write-json
```

### 5. Pipeline / automatización (output JSON)

```bash
python -m sync_catalogos.sync --all --json > /var/log/sync-$(date +%F).json

# Luego, parsear con jq
jq '.[] | select(.error) | .name' < /var/log/sync-2026-05-02.json
jq '[.[] | .rows] | add' < /var/log/sync-2026-05-02.json    # total filas
```

### 6. Dry-run para verificar conectividad sin escribir

```bash
python -m sync_catalogos.sync --all --dry-run --kind reps_export
```

### 7. Re-sync de un solo catálogo cuando cambió la fuente

```bash
# Ej. MinSalud actualizó CIE-10
python -m sync_catalogos.sync --catalog cie10 --i-have-permission

# Verifica el nuevo sha256 en el JSON
jq '.metadata.sha256' catalogos_co/co/clinical/cie10.json
```

---

## Variables de entorno

Definir en `.env` en la raíz del proyecto (o en el ambiente del shell). Ver `.env.example` por referencia.

### Generales

| Variable                  | Default              | Descripción                                          |
|---------------------------|----------------------|------------------------------------------------------|
| `SALUD_CATALOGS_ROOT`     | `./catalogos_co`     | Directorio raíz para los JSON sincronizados          |
| `SALUD_SOCRATA_APP_TOKEN` | (vacío)              | App token Socrata. Sube rate de ~1k/h a ~100k/h     |

### Pool de proxies

| Variable                  | Default              | Descripción                                          |
|---------------------------|----------------------|------------------------------------------------------|
| `PROXY_ENABLED`           | `false`              | Activa el pool global                                |
| `PROXY_USE_FOR_KINDS`     | (auto)               | CSV de kinds. Auto = solo `sispro_aspx`              |
| `PROXY_LIST`              | —                    | Lista CSV de URLs (provider StaticProvider)          |
| `PROXY_LIST_URL`          | —                    | Endpoint HTTP propio (provider HttpProvider)         |
| `TWOCAPTCHA_API_KEY`      | —                    | Provider TwoCaptcha residential                      |
| `PROXY_COUNTRY`           | mix                  | ISO 2 letras (co, us, mx, ...)                       |
| `PROXY_PROTOCOL`          | (todos)              | `http` | `https` | `socks5` ; vacío = los 3 (mejor fallback) |
| `PROXY_POOL_SIZE`         | `10`                 | 1..2000                                              |
| `PROXY_REFRESH_MINUTES`   | `30`                 | Cada cuánto re-pregunta al provider                  |
| `PROXY_FAIL_THRESHOLD`    | `3`                  | Fallos consecutivos antes de cooldown                |
| `PROXY_COOLDOWN_SECONDS`  | `300`                | Cuánto descansa una IP unhealthy                     |
| `PROXY_MAX_ATTEMPTS`      | `6`                  | Cuántos proxies probar antes de fallback a directo   |

Más detalle en [proxy.md](proxy.md).

---

## Output

### Resumen humano (default)

```
Sincronizados: 12  con error: 1  saltados: 4
  ✓ divipola_departamentos          33   0.5s  → catalogos_co/co/geo/...
  ✓ divipola_municipios           1122   1.0s  → ...
  ✓ reps_sedes                   76561  17.3s  → ...
  ✓ reps_servicios              228293 161.4s  → ...
  ...
  ✗ sispro_table_x                       ERROR: HTTPError 500
  · cie10                              skip: requiere flag --i-have-permission
  · cups                               skip: requiere flag --i-have-permission
```

### JSON (para pipelines)

Cada elemento tiene esta forma:
```json
[
  {
    "name": "divipola_municipios",
    "kind": "socrata",
    "rows": 1122,
    "version": "2025-01-24T20:44:32+00:00",
    "sha256_short": "5964193765e8",
    "duration_s": 1.0,
    "sinks": ["json", "db"],
    "path": "/.../catalogos_co/co/geo/divipola_municipios.json"
  },
  {
    "name": "sispro_table_x",
    "error": "HTTPError 500",
    "duration_s": 0.3
  },
  {
    "name": "cie10",
    "kind": "sispro_aspx",
    "skipped": true,
    "reason": "requiere flag --i-have-permission",
    "consent_reason": "El robots.txt de web.sispro.gov.co tiene...",
    "path": "/.../co/clinical/cie10.json"
  }
]
```

### Exit code

- `0` — todos los catálogos OK (incluso si hubo skipped)
- `≠0` — al menos un catálogo dio error

Esto es lo que cron debe verificar.

---

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

Un archivo por catálogo:
```json
{
  "metadata": {
    "name": "reps_sedes",
    "description": "REPS — Sedes (≈76.6k con dirección, barrio, tel, email, gerente)",
    "source": "reps_export",
    "source_url": "https://prestadores.minsalud.gov.co/habilitacion/consultas/sedes_reps.aspx",
    "source_id": "sedes_reps.aspx",
    "version": "2026-05-02T20:22:00Z",
    "license": "MinSalud REPS — Registro Especial de Prestadores (consulta pública)",
    "row_count": 76561,
    "last_synced": "2026-05-02T20:22:00Z",
    "sha256": "ef9e2ced00ff..."
  },
  "entries": [
    {"departamento": "Amazonas", "municipio": "EL ENCANTO", ...},
    ...
  ]
}
```

---

## Inspeccionar resultados

### Listar todos los catálogos sincronizados

```bash
find catalogos_co -name '*.json' | sort
```

### Ver metadata sin cargar todo el archivo

```bash
jq '.metadata' catalogos_co/co/institutional/reps_sedes.json
```

### Filtrar entries

```bash
# Top 5 sedes en Bogotá
jq '.entries | map(select(.departamento == "Bogotá D.C")) | .[:5]' \
   catalogos_co/co/institutional/reps_sedes.json

# Conteo de filas con descripción no vacía en CIE10
jq '.entries | map(select(.Descripcion != "")) | length' \
   catalogos_co/co/clinical/cie10.json
```

### Verificar integridad

```bash
# El sha256 debe coincidir con el de las entries serializadas
jq '.metadata.sha256' catalogos_co/co/clinical/cie10.json

# Si quieres recalcular y comparar:
python -c "
import json, hashlib
data = json.load(open('catalogos_co/co/clinical/cie10.json'))
body = json.dumps(data['entries'], ensure_ascii=False, sort_keys=True, separators=(',', ':'))
print(hashlib.sha256(body.encode()).hexdigest())
print('vs metadata:', data['metadata']['sha256'])
"
```

---

## Inspeccionar resultados en DB

### Postgres / MySQL / MSSQL

```sql
-- Lista de catálogos persistidos
SELECT name, source, row_count, last_synced, table_name
FROM salud_catalog_metadata
ORDER BY name;

-- Ver schema inferido de un catálogo
SELECT schema_json FROM salud_catalog_metadata WHERE name = 'reps_sedes';

-- Consultar la tabla del catálogo
SELECT * FROM salud_reps_sedes WHERE municipio = 'MEDELLÍN' LIMIT 10;

-- JOIN cross-catalog
SELECT m.cod_dpto, d.nombre_departamento, m.nom_mpio
FROM salud_divipola_municipios m
JOIN salud_divipola_departamentos d ON m.cod_dpto = d.codigo_departamento
WHERE m.nom_mpio LIKE 'PUERTO%';
```

### MongoDB

```js
// Lista de catálogos
db.salud_catalog_metadata.find({}, {name:1, row_count:1, _id:0}).sort({name:1})

// Schema inferido de un catálogo
db.salud_catalog_metadata.findOne({name: "reps_sedes"}).schema

// Consulta sobre la colección del catálogo
db.salud_reps_sedes.find({municipio: "MEDELLÍN"}).limit(10)

// Aggregation pipeline cross-collection ($lookup)
db.salud_divipola_municipios.aggregate([
  {$group: {_id: "$dpto", n: {$sum: 1}}},
  {$sort: {n: -1}},
  {$limit: 5}
])
```

---

## Troubleshooting

### "requires --i-have-permission flag"

El catálogo es de SISPRO. Añade el flag y documenta la ejecución:

```bash
python -m sync_catalogos.sync --catalog cie10 --i-have-permission
```

### Conexión DB falla con "database does not exist"

Crea la DB antes:

```bash
# Postgres
psql -U postgres -c "CREATE DATABASE salud"

# MySQL
mysql -u root -e "CREATE DATABASE salud"

# Mongo se autocrea al primer write
```

### Proxy devuelve HTTP 407

Tu IP no está whitelisted en el proveedor. Diagnóstico:

```bash
python -m sync_catalogos.proxy_check
```

Si tu IP no aparece en `ip_white`, agrégala en el panel del proveedor (ej. https://2captcha.com/setting/ip-whitelist).

Mientras tanto, el sync sigue funcionando vía fallback automático a directo.

### El sync de un catálogo SISPRO devuelve 0 filas

Algunos códigos SISPRO requieren filtros adicionales (fechas, etc.) o están descontinuados. Inspecciona manualmente:

```bash
curl "https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=<CODE>"
```

Si es realmente vacío, marca el catálogo como inactivo en `sources.py` (o ignóralo).

### El export REPS tarda mucho (>5 min)

`reps_servicios` es el catálogo más grande (~228k filas, 155 MB CSV). Es normal que tarde 90-120 s. Si tarda más:
- Verifica conectividad: `curl -I https://prestadores.minsalud.gov.co/habilitacion/work.aspx`
- Verifica si el proxy está activo y agotando reintentos: `python -m sync_catalogos.proxy_check`

### Postgres "value too long for type character varying(N)"

El schema inferido usó una longitud insuficiente. Esto NO debería pasar (el inference usa max_observed + 25% buffer sobre TODAS las filas). Si pasa, es bug — abrir issue con el catálogo y la fila ofensora.

Workaround inmediato: drop la tabla y re-syncrear (el schema se regenera del 0):

```sql
DROP TABLE salud_<catalog_name>;
```

```bash
python -m sync_catalogos.sync --catalog <catalog_name> --db ...
```

---

## Próxima lectura

- [Despliegue](06-despliegue.md) — cron, Docker, monitoring
- [Pruebas](07-pruebas.md) — validación pre-producción

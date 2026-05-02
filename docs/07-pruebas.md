# 7. Pruebas

Estrategia de validación: **smoke tests + checks post-sync + benchmarks**. Sin suite de unit tests pesada — el valor del proyecto está en que **funciona contra los endpoints reales**, no en mocks.

## Niveles de prueba

| Nivel             | Pregunta que responde                              | Frecuencia        |
|-------------------|----------------------------------------------------|-------------------|
| **1. Conectividad** | ¿Las 3 fuentes responden?                          | Antes de cada deploy |
| **2. Smoke por kind** | ¿Cada cliente parsea correctamente su formato?    | Antes de cada deploy |
| **3. Schema integrity** | ¿Los datos no han cambiado de forma destructiva? | Cada sync exitoso |
| **4. End-to-end con DB** | ¿Sinks SQL/Mongo escriben datos consultables? | Antes de tocar prod |
| **5. Performance bench** | ¿Tiempos están en línea con baseline?           | Trimestralmente   |
| **6. Idempotencia**  | ¿Re-correr produce el mismo estado?               | Antes de tocar prod |

---

## Nivel 1 — Conectividad básica

Verifica que las 3 fuentes están accesibles desde el server.

```bash
# Datos Abiertos
curl -sI https://www.datos.gov.co/resource/c36g-9fc2.json | head -1
# → HTTP/2 200

# REPS Habilitación
curl -sI https://prestadores.minsalud.gov.co/habilitacion/work.aspx | head -1
# → HTTP/1.1 200

# SISPRO
curl -sI https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=Etnia | head -1
# → HTTP/1.1 200
```

Si alguna devuelve 4xx/5xx, no es problema del proyecto sino de la fuente o de la red.

---

## Nivel 2 — Smoke por kind (1 catálogo de cada uno)

```bash
# Sin DB, dry-run no funciona (necesita escribir para validar parsing)
# usar catálogos chicos para que sea rápido

# 1) Socrata
python -m sync_catalogos.sync --catalog divipola_departamentos
# Esperado: ✓ 33 filas, ~1s

# 2) REPS
python -m sync_catalogos.sync --catalog reps_sanciones
# Esperado: ✓ ~700 filas, ~2s

# 3) SISPRO (requiere consent)
python -m sync_catalogos.sync --catalog sispro_etnia --i-have-permission
# Esperado: ✓ 6 filas, ~1s
```

### Validación del JSON resultante

```bash
python <<'PY'
import json, hashlib
from pathlib import Path

for path in [
    "catalogos_co/co/geo/divipola_departamentos.json",
    "catalogos_co/co/institutional/reps_sanciones.json",
    "catalogos_co/co/admin/sispro_etnia.json",
]:
    cat = json.loads(Path(path).read_text(encoding="utf-8"))
    m = cat["metadata"]
    n = len(cat["entries"])

    # 1. metadata completa
    for f in ("name","source","source_url","row_count","last_synced","sha256"):
        assert m.get(f) is not None, f"{path} missing {f}"

    # 2. row_count coincide
    assert m["row_count"] == n, f"{path} row_count mismatch"

    # 3. sha256 reproducible
    body = json.dumps(cat["entries"], ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    expected = hashlib.sha256(body.encode("utf-8")).hexdigest()
    assert m["sha256"] == expected, f"{path} sha256 mismatch"

    # 4. entries no vacías
    assert n > 0, f"{path} sin filas"
    assert isinstance(cat["entries"][0], dict), f"{path} entries no son dicts"

    print(f"  ✓ {path}  ({n} filas, sha256 OK)")

print("\nNivel 2 OK")
PY
```

---

## Nivel 3 — Schema integrity post-sync

Detecta cambios destructivos en los catálogos (columnas que desaparecen, filas que caen drásticamente, etc.).

### Comparar contra snapshot anterior

```bash
python <<'PY'
import json
from pathlib import Path

# Asume que tienes un baseline en /var/lib/co-salud-catalogos/baseline/
BASELINE = Path("/var/lib/co-salud-catalogos/baseline")
CURRENT  = Path("catalogos_co")

for path in CURRENT.rglob("*.json"):
    rel = path.relative_to(CURRENT)
    base = BASELINE / rel
    if not base.exists():
        continue
    cur_meta = json.loads(path.read_text(encoding="utf-8"))["metadata"]
    base_meta = json.loads(base.read_text(encoding="utf-8"))["metadata"]

    # 1. Row count no debe caer >10%
    diff_pct = (cur_meta["row_count"] - base_meta["row_count"]) / max(base_meta["row_count"], 1) * 100
    if diff_pct < -10:
        print(f"  ⚠ {rel}: row_count cayó {diff_pct:.1f}%")

    # 2. Cambio de sha256 = data cambió (info, no warning)
    if cur_meta["sha256"] != base_meta["sha256"]:
        print(f"  · {rel}: cambió sha256 (delta: {diff_pct:+.1f}%)")
PY
```

### Schema diff con DB

```sql
-- Postgres: compara columnas actuales vs schema_json registrado
SELECT m.name, m.schema_json::jsonb AS registered_schema,
       jsonb_agg(c.column_name) AS current_columns
FROM salud_catalog_metadata m
JOIN information_schema.columns c
  ON c.table_schema = 'public' AND c.table_name = m.table_name
WHERE m.schema_json IS NOT NULL
GROUP BY m.name, m.schema_json;
```

---

## Nivel 4 — End-to-end con DB

Levanta motores temporales (Docker) y valida que lectura/escritura funcionan.

### Postgres

```bash
# Setup
docker run -d --name test-pg -e POSTGRES_PASSWORD=test -p 55432:5432 postgres:16
sleep 5
docker exec test-pg psql -U postgres -c "CREATE DATABASE salud_test"

PG_URL="postgresql+psycopg://postgres:test@localhost:55432/salud_test"

# Sync 3 catálogos
python -m sync_catalogos.sync --catalog divipola_municipios --db "$PG_URL"
python -m sync_catalogos.sync --catalog sispro_etnia --i-have-permission --db "$PG_URL"
python -m sync_catalogos.sync --catalog reps_sanciones --db "$PG_URL"

# Verificar
docker exec test-pg psql -U postgres -d salud_test -c "
SELECT name, table_name, row_count FROM salud_catalog_metadata ORDER BY name;
SELECT count(*) AS catalog_tables
  FROM information_schema.tables
  WHERE table_schema='public' AND table_name LIKE 'salud_%';
"

# Validar acentos preservados
docker exec test-pg psql -U postgres -d salud_test -c "
SELECT nom_mpio FROM salud_divipola_municipios
WHERE nom_mpio LIKE 'MEDELL%' OR nom_mpio LIKE 'BOGOT%';
"

# Validar tipos inferidos
docker exec test-pg psql -U postgres -d salud_test -c "
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name='salud_sispro_etnia';
"
# Esperado: codigo BIGINT, habilitado BOOLEAN, nombre VARCHAR(100), ...

# Cleanup
docker rm -f test-pg
```

### MongoDB

```bash
docker run -d --name test-mg -p 27018:27017 mongo:7
sleep 3

MG_URL="mongodb://localhost:27018/salud_test"

python -m sync_catalogos.sync --catalog divipola_municipios --db "$MG_URL"

docker exec test-mg mongosh --quiet salud_test --eval '
print("Collections: " + db.getCollectionNames().length);
print("Sample doc:");
printjson(db.salud_divipola_municipios.findOne({nom_mpio: "MEDELLÍN"}));
print("\nSchema en metadata:");
db.salud_catalog_metadata.findOne({name: "divipola_municipios"}).schema.forEach(s =>
  print(`  ${s.col} - ${s.type}`)
);
'

docker rm -f test-mg
```

### MySQL / MSSQL

Mismo flujo con `mysql:8` / `mcr.microsoft.com/mssql/server:2022-latest`. La codepath es la misma SQLAlchemy → solo cambia el dialect en la URL.

---

## Nivel 5 — Performance benchmark

Baseline conocido (M1 Mac, 16 GB RAM, conexión doméstica COL):

| Operación                              | Tiempo baseline | Notas                      |
|----------------------------------------|----------------:|----------------------------|
| `divipola_departamentos` (33 filas)    | ~1.0 s          | Latencia red ≫ procesamiento |
| `divipola_municipios` (1.122 filas)    | ~1.0 s          |                            |
| `cie10` (14k filas, 7 páginas SISPRO)  | ~10 s           | 1 página/s                 |
| `cups` (12k filas)                     | ~8 s            |                            |
| `reps_sedes` (76k filas, 31 MB CSV)    | ~17 s           |                            |
| `reps_servicios` (228k filas, 155 MB)  | ~95 s           | Bottleneck: red + parsing  |
| Bulk Postgres (273 catálogos chicos)   | ~4 s            | 1700 filas/s               |
| Bulk MongoDB (273 catálogos chicos)    | ~4 s            |                            |
| Sync masivo SISPRO (297 catálogos)     | ~25 min         | 1.9M filas                 |

### Bench script

```bash
python <<'PY'
import time, json
from sync_catalogos.sync import sync_one
from sync_catalogos.sources import find

cases = [
    "divipola_departamentos",
    "divipola_municipios",
    "sispro_etnia",
    "reps_sanciones",
    "cie10",
]
results = []
for name in cases:
    src = find(name)
    if not src:
        continue
    t0 = time.time()
    r = sync_one(src, consent=True)
    elapsed = time.time() - t0
    results.append((name, r.get("rows", 0), elapsed))
    print(f"  {name:40s} {r.get('rows',0):>7} filas  {elapsed:.2f}s")

# Comparar con baseline
print("\nBaseline (esperado):")
print("  divipola_departamentos  33 filas  ~1.0s")
print("  divipola_municipios   1122 filas  ~1.0s")
print("  sispro_etnia             6 filas  ~1.0s")
print("  reps_sanciones        ~700 filas  ~2.0s")
print("  cie10               ~14000 filas ~10.0s")
PY
```

Si tiempos exceden 2× el baseline:
- Verificar latencia de red al server destino: `ping www.datos.gov.co`
- Verificar si hay proxy activo agotando reintentos: `python -m sync_catalogos.proxy_check`
- Revisar logs del scraper específico

---

## Nivel 6 — Idempotencia

Re-correr el mismo sync debe producir exactamente el mismo estado.

```bash
# 1. Sync inicial
python -m sync_catalogos.sync --catalog divipola_municipios
SHA1=$(jq -r '.metadata.sha256' catalogos_co/co/geo/divipola_municipios.json)

# 2. Re-sync inmediatamente
python -m sync_catalogos.sync --catalog divipola_municipios
SHA2=$(jq -r '.metadata.sha256' catalogos_co/co/geo/divipola_municipios.json)

# 3. sha256 de datos debe ser igual (los datos no cambian en la fuente entre 2 syncs)
if [ "$SHA1" = "$SHA2" ]; then
    echo "  ✓ Idempotente: $SHA1"
else
    echo "  ⚠ Datos cambiaron entre syncs: $SHA1 → $SHA2"
fi
```

Postgres / Mongo: corre dos veces y verifica que no hay duplicación.

```sql
-- Postgres: row_count debe ser igual antes y después de re-sync
SELECT row_count FROM salud_catalog_metadata WHERE name = 'divipola_municipios';
-- Re-sync ↑
SELECT row_count FROM salud_catalog_metadata WHERE name = 'divipola_municipios';
```

---

## Validación pre-producción (checklist)

Antes de promocionar a producción, validar todos estos:

```
[ ] git clone funcional desde el repo
[ ] uv pip install -e ".[postgres,mongo]" sin errores
[ ] python -m sync_catalogos.sync --list muestra 319 catálogos
[ ] Conectividad a las 3 fuentes (curl -I)
[ ] Smoke nivel 2 — 1 catálogo de cada kind sincroniza OK
[ ] Validación de JSON: row_count, sha256, metadata completa
[ ] DB sink contra Postgres temporal: tablas creadas, datos consultables
[ ] DB sink contra MongoDB temporal: idem
[ ] Acentos preservados en values (MEDELLÍN, BOGOTÁ, ARCHIPIÉLAGO...)
[ ] Tipos inferidos correctos (BIGINT, BOOLEAN, DATE detectados)
[ ] Idempotencia: re-sync da mismo sha256 / row_count
[ ] Permisos en disco (.env 600, datos 644)
[ ] Permisos en DB (usuario writer + reader separados)
[ ] Cron schedulado y log rotation configurada
[ ] Secret manager para credenciales sensibles
[ ] Alerta operativa para exit code != 0 del cron
```

---

## Validación de regresión continua

Para CI / GitHub Actions, ejemplo mínimo:

```yaml
# .github/workflows/smoke.yml
name: smoke
on:
  schedule:
    - cron: "0 12 * * *"   # diario al mediodía UTC
  workflow_dispatch:

jobs:
  smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv pip install --system -e .
      - name: Smoke Socrata
        run: python -m sync_catalogos.sync --catalog divipola_departamentos
      - name: Smoke REPS
        run: python -m sync_catalogos.sync --catalog reps_sanciones
      - name: Validate JSON
        run: |
          python -c "
          import json, sys
          for p in ['catalogos_co/co/geo/divipola_departamentos.json',
                    'catalogos_co/co/institutional/reps_sanciones.json']:
              cat = json.load(open(p))
              assert cat['metadata']['row_count'] > 0
              assert cat['metadata']['sha256']
              assert len(cat['entries']) == cat['metadata']['row_count']
          print('OK')
          "
```

---

## Troubleshooting de pruebas

### "ImportError: No module named 'sqlalchemy'"

Falta el extra:
```bash
uv pip install -e ".[db]"   # o [postgres] [mysql] [mssql] [mongo]
```

### "psycopg.errors.StringDataRightTruncation"

Schema inferido fue insuficiente para algún valor. Es bug — no debería pasar (inference usa max sobre todas las filas + 25% buffer). Fix:

```sql
DROP TABLE salud_<catalog_name>;   -- regenera con nuevo max
```

```bash
python -m sync_catalogos.sync --catalog <name> --db "$DB_URL"
```

Y reportar el catálogo + valor ofensor para investigar.

### "InvalidDocument: cannot encode object: datetime.date"

Solo pasa con MongoDB. Bug fixed en commit `4066146` — promueve `date` → `datetime`. Asegurar versión del repo actualizada.

### Smoke contra REPS tarda mucho (>30s para sanciones)

Posibles causas:
- Proxy activado y agotando reintentos. Desactivar para test:
  ```bash
  PROXY_ENABLED=false python -m sync_catalogos.sync --catalog reps_sanciones
  ```
- Latencia de red alta al server colombiano. Considerar correr el smoke desde una región más cercana.

### MongoDB drop entire test DB

```bash
docker exec test-mg mongosh --quiet salud_test --eval 'db.dropDatabase()'
```

---

## Próxima lectura

- [Manual de uso](04-manual-uso.md) — referencia de comandos para la operación diaria
- [Despliegue](06-despliegue.md) — operación en producción

# 6. Despliegue

## Modos soportados

| Modo                  | Quién lo usa            | Frecuencia              | Persistencia                |
|-----------------------|-------------------------|-------------------------|-----------------------------|
| **Local dev**         | Desarrolladores         | ad-hoc                  | JSON en disco               |
| **Server con cron**   | Equipos operativos      | semanal / trimestral    | JSON + DB opcional          |
| **Container Docker**  | Producción multitenant  | scheduled job           | DB centralizada             |
| **Kubernetes CronJob**| Cloud-native            | scheduled job           | DB centralizada             |

---

## Local dev

```bash
git clone https://github.com/orlandobcr/co-salud-catalogos
cd co-salud-catalogos
uv venv
uv pip install -e .

# Verificar
python -m sync_catalogos.sync --list
python -m sync_catalogos.sync --catalog divipola_departamentos
```

Sin más infra. Datos quedan en `./catalogos_co/`.

Para incluir DB sink en dev:
```bash
uv pip install -e ".[postgres]"   # o [mysql] [mssql] [mongo]
```

---

## Server con cron (recomendado para CAC)

### Instalación

```bash
# En el server (Ubuntu / Debian / RHEL)
sudo useradd -r -m -d /opt/co-salud-catalogos co-salud
sudo chown -R co-salud:co-salud /opt/co-salud-catalogos
sudo -u co-salud bash <<'EOF'
cd /opt/co-salud-catalogos
git clone https://github.com/orlandobcr/co-salud-catalogos .
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv venv
uv pip install -e ".[postgres]"   # según motor destino
EOF
```

### Configuración (.env del server)

```bash
sudo -u co-salud nano /opt/co-salud-catalogos/.env
```

Contenido:
```dotenv
SALUD_CATALOGS_ROOT=/var/lib/co-salud-catalogos/json
SALUD_SOCRATA_APP_TOKEN=<tu-app-token>

# DB destino
# (no se pone aquí — se pasa via --db en el cron, así no expone secrets en proceso list)

# Proxy desactivado por default
PROXY_ENABLED=false
```

Asegurar permisos:
```bash
sudo chmod 600 /opt/co-salud-catalogos/.env
sudo chown co-salud:co-salud /opt/co-salud-catalogos/.env
sudo mkdir -p /var/lib/co-salud-catalogos/json
sudo chown -R co-salud:co-salud /var/lib/co-salud-catalogos
sudo mkdir -p /var/log/co-salud-catalogos
sudo chown co-salud:co-salud /var/log/co-salud-catalogos
```

### Cron

```bash
sudo -u co-salud crontab -e
```

```cron
# Variables
PATH=/home/co-salud/.local/bin:/usr/local/bin:/usr/bin:/bin
HOME=/home/co-salud
SHELL=/bin/bash
DB_URL=postgresql+psycopg://salud_user:secret@db.example.com:5432/salud

# Lunes 03:00 UTC — REPS Habilitación (semanal)
0 3 * * 1 cd /opt/co-salud-catalogos && uv run python -m sync_catalogos.sync \
    --all --kind reps_export --db "$DB_URL" \
    --json >> /var/log/co-salud-catalogos/reps-$(date +\%F).json 2>&1

# Lunes 04:00 UTC — Datos Abiertos (semanal)
0 4 * * 1 cd /opt/co-salud-catalogos && uv run python -m sync_catalogos.sync \
    --all --kind socrata --db "$DB_URL" \
    --json >> /var/log/co-salud-catalogos/socrata-$(date +\%F).json 2>&1

# IMPORTANTE: SISPRO NO se pone en cron.
# Cada ejecución debe ser manual y documentada en bitácora.
# Comando manual:
# uv run python -m sync_catalogos.sync --all --kind sispro_aspx \
#     --i-have-permission --db "$DB_URL" --json
```

### Verificar el cron

```bash
# Ver últimos logs
ls -la /var/log/co-salud-catalogos/

# Ver el log más reciente
tail -50 /var/log/co-salud-catalogos/reps-2026-05-04.json

# Verificar metadata en DB
psql -h db.example.com -U salud_user -d salud -c "
SELECT name, last_synced, row_count
FROM salud_catalog_metadata
WHERE last_synced > NOW() - interval '7 days'
ORDER BY last_synced DESC;
"
```

### Alertas

Cron envía email del exit code != 0 por default. Para algo más sofisticado, wrap con `mailx`:

```cron
0 3 * * 1 cd /opt/co-salud-catalogos && \
    (uv run python -m sync_catalogos.sync --all --kind reps_export --db "$DB_URL" --json \
     >> /var/log/co-salud-catalogos/reps-$(date +\%F).json 2>&1 || \
     mailx -s "[ALERTA] sync REPS falló" ops@example.com < /var/log/co-salud-catalogos/reps-$(date +\%F).json)
```

---

## Container Docker

### Dockerfile

```dockerfile
FROM python:3.13-slim

# uv para instalación rápida
RUN pip install --no-cache-dir uv

# Sistema mínimo (lxml necesita headers)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libxml2 libxslt1.1 ca-certificates tini && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml README.md ./
COPY sync_catalogos ./sync_catalogos

# Instalar con todos los drivers
RUN uv pip install --system -e ".[postgres,mysql,mongo]"

# Volumen para los JSON sincronizados
VOLUME ["/data/catalogos_co"]
ENV SALUD_CATALOGS_ROOT=/data/catalogos_co

# tini como PID 1 para signal handling
ENTRYPOINT ["tini", "--"]
CMD ["python", "-m", "sync_catalogos.sync", "--list"]
```

### Build + run

```bash
docker build -t co-salud-catalogos:0.1 .

# Sync REPS a Postgres (containerizado)
docker run --rm --name salud-sync \
    -v co-salud-data:/data/catalogos_co \
    -e SALUD_SOCRATA_APP_TOKEN \
    co-salud-catalogos:0.1 \
    python -m sync_catalogos.sync --all --kind reps_export \
        --db "postgresql+psycopg://user:pass@host.docker.internal:5432/salud"
```

### docker-compose

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: salud
      POSTGRES_USER: salud
      POSTGRES_PASSWORD_FILE: /run/secrets/db_pass
    volumes:
      - pgdata:/var/lib/postgresql/data
    secrets:
      - db_pass

  sync-reps:
    image: co-salud-catalogos:0.1
    depends_on: [postgres]
    volumes:
      - catalogos:/data/catalogos_co
    environment:
      DB_URL: "postgresql+psycopg://salud:${DB_PASS}@postgres:5432/salud"
    command: >
      python -m sync_catalogos.sync --all --kind reps_export
      --db "${DB_URL}" --json
    # Para correr 1 vez/semana, usar swarm cron o un orchestrator externo

volumes:
  pgdata:
  catalogos:

secrets:
  db_pass:
    file: ./secrets/db_pass.txt
```

---

## Kubernetes CronJob

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: salud-catalogos-reps
  namespace: salud
spec:
  schedule: "0 3 * * 1"   # Lunes 03:00
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 5
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: sync
              image: ghcr.io/orlandobcr/co-salud-catalogos:0.1
              args:
                - python
                - -m
                - sync_catalogos.sync
                - --all
                - --kind
                - reps_export
                - --db
                - $(DB_URL)
                - --no-write-json
                - --json
              env:
                - name: DB_URL
                  valueFrom:
                    secretKeyRef:
                      name: salud-db
                      key: url
                - name: SALUD_SOCRATA_APP_TOKEN
                  valueFrom:
                    secretKeyRef:
                      name: salud-tokens
                      key: socrata
              resources:
                requests: { cpu: "200m", memory: "512Mi" }
                limits:   { cpu: "1",    memory: "2Gi" }
---
apiVersion: batch/v1
kind: CronJob
metadata:
  name: salud-catalogos-socrata
spec:
  schedule: "0 4 * * 1"   # Lunes 04:00
  jobTemplate:
    # ... idem pero --kind socrata ...
```

Para SISPRO usar `Job` manual (no CronJob) — requiere consentimiento operativo documentado.

---

## Sizing de DB

Estimación basada en sync real (273 catálogos chicos + REPS):

| Catálogo                  | Filas    | Cols  | Postgres tamaño | Mongo tamaño |
|---------------------------|---------:|------:|----------------:|-------------:|
| `divipola_departamentos`  | 33       | 4     | ~16 KB          | ~24 KB       |
| `divipola_municipios`     | 1.122    | 7     | ~150 KB         | ~200 KB      |
| `cie10`                   | 14.000   | 22    | ~6 MB           | ~9 MB        |
| `cups`                    | 12.000   | 22    | ~5 MB           | ~7 MB        |
| `reps_sedes`              | 76.561   | 47    | ~50 MB          | ~80 MB       |
| `reps_servicios`          | 228.293  | 94    | **~250 MB**     | **~400 MB**  |
| **TOTAL (319 catálogos)** | **~2.5M**| —     | **~600 MB**     | **~1 GB**    |

Sizing recomendado:
- **DB instance**: 4 vCPU, 8 GB RAM, 20 GB disk para los catálogos + crecimiento.
- Para Postgres con índices custom: +50% (1 GB).
- Para Mongo con réplica set: ×2 a ×3 (~3 GB).

---

## Variables de entorno en producción

Convención: usar **secret manager** (Vault / AWS Secrets Manager / k8s secrets) en lugar de `.env`.

| Variable                   | Sensibilidad     | Recomendación                                       |
|----------------------------|------------------|-----------------------------------------------------|
| `SALUD_SOCRATA_APP_TOKEN`  | medio            | secret manager                                      |
| `DB_URL` (no es del proyecto, pero típico) | alto | secret manager, NO en argv visible            |
| `TWOCAPTCHA_API_KEY`       | alto             | secret manager                                      |
| `PROXY_LIST`               | alto             | secret manager                                      |
| `SALUD_CATALOGS_ROOT`      | bajo             | env var del container                               |
| `PROXY_ENABLED`, etc.      | bajo             | env var del container                               |

`--db <url>` en argv del proceso queda visible en `ps`. Mejor:

```bash
DB_URL=postgresql+psycopg://... \
    python -m sync_catalogos.sync --all --db "$DB_URL"
```

O futuro: añadir `--db-from-env DB_URL` (TODO).

---

## Logs / observability

### Output del CLI

- Modo human (default): pintado con resumen al final.
- Modo `--json`: stream JSON al stdout. Pipear a archivo / parser.

### Logger interno

```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
```

Eventos clave:
- `sync_catalogos.proxy.proxy.refreshed` — pool actualizado, count
- `sync_catalogos.proxy.proxy.attempt_failed` — proxy individual falló
- `sync_catalogos.proxy.proxy.fallback_direct` — agotaron proxies
- `sync_catalogos.sispro.sispro.empty_page` — paginación vacía detectada

Para integración con sistemas de logs (ELK / Loki / CloudWatch), redirigir stdout/stderr.

### Métricas sugeridas para alertar

| Métrica                                 | Umbral típico               | Acción si excede                   |
|-----------------------------------------|-----------------------------|------------------------------------|
| `% catálogos con error en última corrida` | > 0%                       | Investigar log JSON                |
| `# horas desde último sync exitoso`     | > 168 (1 semana) para REPS  | Alerta a oncall                    |
| `# filas - delta entre sincros`         | > 20% diff                  | Validar manualmente (cambio fuente?)|
| `duración total del sync`               | > 2× promedio               | Ver si SISPRO/REPS está lento      |
| `tamaño DB`                             | > +30% mes/mes              | Revisar si hay duplicación         |

Query para construir las métricas (Postgres):
```sql
-- Catálogos no actualizados en última semana
SELECT name, last_synced
FROM salud_catalog_metadata
WHERE last_synced < NOW() - interval '7 days'
ORDER BY last_synced;

-- Cambio en row count
SELECT name, row_count, last_synced
FROM salud_catalog_metadata
ORDER BY last_synced DESC;
```

---

## Backup / disaster recovery

### Datos

- **JSON en disco**: regenerable con `--all`. NO requiere backup (es derivado).
- **DB**: backup standard (pg_dump, mysqldump, mongodump) con la misma política que el resto del datalake del cliente.
- **Recreación full desde 0**: ~25 min (Datos Abiertos + REPS) + ~25 min (SISPRO con consentimiento) = **~50 min total**.

### Recovery test recomendado

```bash
# Trimestralmente: restore en ambiente staging
pg_restore -d salud_staging /backups/salud-2026-W18.dump

# Validar:
psql -d salud_staging -c "SELECT count(*) FROM salud_catalog_metadata;"
psql -d salud_staging -c "SELECT count(*) FROM salud_reps_sedes;"
```

### Preservar snapshot histórico

Los catálogos cambian con el tiempo. Para auditoría retroactiva:

```sql
-- Crear snapshot mensual con timestamp
CREATE SCHEMA IF NOT EXISTS salud_2026_05;
CREATE TABLE salud_2026_05.divipola_municipios AS
    SELECT * FROM salud_divipola_municipios;
-- ... etc
```

O dump mensual a archivo:
```bash
pg_dump -d salud -n public -f /archive/salud-2026-05.sql
gzip /archive/salud-2026-05.sql
```

El `metadata.sha256` permite detectar si hubo cambio entre snapshots.

---

## Hardening

### Permisos en disco

```bash
# Solo el usuario co-salud lee/escribe
chmod 700 /var/lib/co-salud-catalogos
chmod 600 /opt/co-salud-catalogos/.env
chmod -R 644 /var/lib/co-salud-catalogos/json
```

### Permisos en DB

Crear usuario dedicado solo con permisos necesarios:

```sql
-- Postgres
CREATE USER salud_writer WITH PASSWORD '...';
CREATE DATABASE salud OWNER salud_writer;
GRANT CREATE ON DATABASE salud TO salud_writer;
-- Que pueda crear / dropear / insertar en su propio schema
GRANT USAGE, CREATE ON SCHEMA public TO salud_writer;

-- Y otro usuario solo-lectura para los consumidores (Anonimiz, BI, etc.)
CREATE USER salud_reader WITH PASSWORD '...';
GRANT CONNECT ON DATABASE salud TO salud_reader;
GRANT USAGE ON SCHEMA public TO salud_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO salud_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO salud_reader;
```

### Network

- `co-salud-catalogos` solo necesita salida a:
  - `www.datos.gov.co` (443)
  - `prestadores.minsalud.gov.co` (443)
  - `web.sispro.gov.co` (443)
  - El motor de DB destino
  - (opcional) `api.2captcha.com` (443) si se usa proxy
- No expone puertos.
- No requiere ingress.

Egress allowlist de firewall:
```
allow 443/tcp to www.datos.gov.co
allow 443/tcp to prestadores.minsalud.gov.co
allow 443/tcp to web.sispro.gov.co
allow 5432/tcp to <db host>
```

---

## Migración de versión

Sin breaking changes en el esquema de salida. Para upgrades:

```bash
cd /opt/co-salud-catalogos
sudo -u co-salud git pull
sudo -u co-salud uv pip install -e ".[postgres]" --upgrade

# Re-sync para refrescar metadata (opcional)
sudo -u co-salud python -m sync_catalogos.sync --all --kind socrata
```

Si una versión añade columnas al schema inferido de un catálogo, la próxima corrida del sync reemplaza la tabla con el nuevo schema (DELETE + INSERT). Auditoría: el `schema_json` en `salud_catalog_metadata` cambia entre syncs.

---

## Próxima lectura

- [Pruebas](07-pruebas.md) — validación pre-producción
- [Manual de uso](04-manual-uso.md) — referencia de comandos

# 8. API REST + Dashboard

Capa REST sobre la DB donde el sync persiste los catálogos. Autenticación Bearer JWT, usuarios + permisos por catálogo, documentación OpenAPI/Swagger filtrada dinámicamente según el usuario logueado, y un dashboard web para inspección.

## Componentes

```
┌──────────────────────────────────────────────────────┐
│  Browser / curl / cualquier cliente HTTP             │
└──────────────────────────┬───────────────────────────┘
                           │  Bearer JWT
                           ▼
┌──────────────────────────────────────────────────────┐
│  FastAPI app (sync_catalogos.api.main)               │
│  ├─ /                  landing con login              │
│  ├─ /dashboard         panel autenticado              │
│  ├─ /docs              Swagger dinámico por user      │
│  ├─ /redoc             ReDoc                          │
│  ├─ /openapi.json      spec dinámico                  │
│  ├─ /health                                           │
│  ├─ /auth/login        username + password → JWT      │
│  ├─ /auth/me           info del usuario               │
│  ├─ /catalogs          list (filtrado por permisos)   │
│  ├─ /catalogs/{name}   metadata + schema              │
│  ├─ /catalogs/{name}/entries  filas paginadas         │
│  └─ /admin/*           (solo super_admin)             │
└──────────────────────────┬───────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│  DB (Postgres / MySQL / MSSQL / SQLite)              │
│  ├─ salud_catalog_metadata     (1 fila por catálogo) │
│  ├─ salud_<catalog>            (datos tipados)        │
│  ├─ api_users                                         │
│  ├─ api_user_permissions                              │
│  └─ api_audit_log                                     │
└──────────────────────────────────────────────────────┘
```

## Roles y permisos

Solo dos roles:

| Rol            | Acceso                                                           |
|----------------|------------------------------------------------------------------|
| `super_admin`  | Total. Ve todos los catálogos. Único que puede `/admin/*`        |
| `regular`      | Solo los catálogos en su tabla `api_user_permissions`            |

Permiso por catálogo (no por kind ni por área). Granular y auditable.

## Setup

### 1. Instalar el extra de la API

```bash
uv pip install -e ".[api]"          # FastAPI + uvicorn + JWT + bcrypt
# Más el extra del motor que uses:
uv pip install -e ".[api,postgres]" # o [mysql] / [mssql] / [mongo no aplica para API]
```

> Mongo no se soporta como backend de la API (la API usa SQLAlchemy para queries dinámicas). Si sincronizas a Mongo, también puedes sincronizar a SQL para que la API consuma de ahí.

### 2. Sincronizar datos a la DB

```bash
DB_URL="postgresql+psycopg://user:pass@host:5432/salud"
python -m sync_catalogos.sync --all --kind socrata --db "$DB_URL"
python -m sync_catalogos.sync --all --kind reps_export --db "$DB_URL"
```

### 3. Bootstrap API (crea tablas + super_admin)

```bash
export SALUD_API_DB_URL="$DB_URL"
export SALUD_API_JWT_SECRET=$(openssl rand -hex 32)

python -m sync_catalogos.api.bootstrap --create-superadmin admin
# (prompts password, mínimo 8 chars)
```

### 4. Levantar el server

```bash
uvicorn sync_catalogos.api.main:app --host 0.0.0.0 --port 8000

# o en producción
uvicorn sync_catalogos.api.main:app \
    --host 0.0.0.0 --port 8000 --workers 4 \
    --proxy-headers --forwarded-allow-ips '*'
```

Abrir:
- `http://localhost:8000/` — landing con login
- `http://localhost:8000/dashboard` — panel (tras login)
- `http://localhost:8000/docs` — Swagger dinámico
- `http://localhost:8000/redoc` — ReDoc

## Variables de entorno

Prefijo `SALUD_API_` (todas leídas también desde `.env`):

| Variable                 | Default              | Descripción                                    |
|--------------------------|----------------------|------------------------------------------------|
| `SALUD_API_DB_URL`       | `sqlite:///./salud.db` | URL SQLAlchemy. Debe apuntar a la DB del sync |
| `SALUD_API_JWT_SECRET`   | (obligatorio)        | Secreto HMAC. Generar con `openssl rand -hex 32` |
| `SALUD_API_JWT_ALGORITHM`| `HS256`              | Algoritmo JWT                                   |
| `SALUD_API_JWT_EXPIRE_MINUTES` | `480` (8h)     | Duración del token                              |
| `SALUD_API_BIND_HOST`    | `0.0.0.0`            | Solo informativo (uvicorn lee de su CLI)       |
| `SALUD_API_BIND_PORT`    | `8000`               | Solo informativo                                |
| `SALUD_API_CORS_ORIGINS` | `["*"]`              | Lista JSON                                      |
| `SALUD_API_PAGE_SIZE_DEFAULT` | `100`           | Default `?limit=`                               |
| `SALUD_API_PAGE_SIZE_MAX` | `5000`              | Max `?limit=`                                   |

## Endpoints (resumen)

### Auth

| Método | Path           | Acceso     | Uso                                                |
|--------|----------------|------------|----------------------------------------------------|
| POST   | `/auth/login`  | público    | `{"username","password"}` → token                  |
| GET    | `/auth/me`     | autenticado| Datos del usuario + permisos                       |

### Catalogs

| Método | Path                          | Acceso         | Uso                                          |
|--------|-------------------------------|----------------|----------------------------------------------|
| GET    | `/catalogs`                   | autenticado    | Lista filtrada por permisos                  |
| GET    | `/catalogs/{name}`            | autenticado +permiso | Metadata + schema inferido            |
| GET    | `/catalogs/{name}/entries`    | autenticado +permiso | Filas paginadas: `?limit=&offset=&q=` |

### Admin (solo super_admin)

| Método | Path                                          | Uso                              |
|--------|-----------------------------------------------|----------------------------------|
| GET    | `/admin/users`                                | Lista usuarios                   |
| POST   | `/admin/users`                                | Crea usuario + permisos iniciales|
| PATCH  | `/admin/users/{id}`                           | Update password / role / activo  |
| DELETE | `/admin/users/{id}`                           | Soft delete (is_active=false)    |
| POST   | `/admin/users/{id}/permissions`               | Otorga permisos                  |
| DELETE | `/admin/users/{id}/permissions/{catalog}`     | Revoca un permiso                |
| GET    | `/admin/catalog-options`                      | Lista de catálogos para UI       |
| GET    | `/admin/audit`                                | Log de auditoría                 |

## Documentación dinámica

`/openapi.json` y `/docs` cambian según el bearer token presentado:

- **Sin token**: spec base sin restricciones
- **super_admin**: `path /catalogs/{name}` muestra `enum: [todos los catálogos]`
- **regular user**: `path /catalogs/{name}` muestra `enum: [solo sus catálogos permitidos]`

Esto permite que Swagger UI muestre un **dropdown** con los nombres válidos cuando el usuario está autenticado:

```bash
# Token sin login
curl -s http://localhost:8000/openapi.json | jq '.paths."/catalogs/{name}".get.parameters[0].schema'
# → {"type": "string", "title": "Name"}

# Token de admin
curl -s http://localhost:8000/openapi.json -H "Authorization: Bearer $ADMIN_TOKEN" \
    | jq '.paths."/catalogs/{name}".get.parameters[0].schema.enum | length'
# → 319

# Token de alice (1 permiso)
curl -s http://localhost:8000/openapi.json -H "Authorization: Bearer $ALICE_TOKEN" \
    | jq '.paths."/catalogs/{name}".get.parameters[0].schema.enum'
# → ["sispro_etnia"]
```

El Swagger UI (`/docs`) carga el `/openapi.json` con el bearer del navegador (vía `Authorize` button en la UI), así que muestra el enum filtrado live.

## Dashboard

`http://localhost:8000/` redirige a `/dashboard` si hay token válido en localStorage.

Funcionalidad:

- **Login** (landing) que llena localStorage con `{access_token, username, role, expires_in}`
- **Stats top**: catálogos visibles, filas totales, última sync, # fuentes
- **Card de consumo API**: token con botón copy, ejemplo curl, link a Swagger
- **Filtros**: búsqueda por nombre, dropdown por fuente
- **Tabla** de catálogos con: nombre, fuente, filas, última sync (relativa), tabla SQL
- **Modal de detalle** por catálogo: metadata completa, esquema inferido (todas las columnas con su tipo), muestra de 10 filas

Todo se filtra automáticamente según el usuario logueado: alice solo ve sus 5 catálogos permitidos, admin ve los 319.

## Ejemplos de uso (cliente curl)

### Login y obtener token

```bash
TOKEN=$(curl -s -X POST http://localhost:8000/auth/login \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"admin1234"}' | jq -r .access_token)
```

### Listar catálogos

```bash
curl -s http://localhost:8000/catalogs -H "Authorization: Bearer $TOKEN" | jq
```

### Metadata + schema de un catálogo

```bash
curl -s http://localhost:8000/catalogs/divipola_municipios -H "Authorization: Bearer $TOKEN" | jq
```

### Buscar filas

```bash
curl -s "http://localhost:8000/catalogs/divipola_municipios/entries?q=MEDELL&limit=5" \
    -H "Authorization: Bearer $TOKEN" | jq '.entries'
```

### Crear regular user con 3 permisos (super_admin)

```bash
curl -s -X POST http://localhost:8000/admin/users \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "username": "alice",
        "password": "alice1234",
        "role": "regular",
        "permissions": ["divipola_municipios", "cie10", "cups"]
    }'
```

### Otorgar permiso adicional

```bash
curl -s -X POST http://localhost:8000/admin/users/2/permissions \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"catalog_names": ["reps_sedes"]}'
```

### Revocar permiso

```bash
curl -s -X DELETE http://localhost:8000/admin/users/2/permissions/cie10 \
    -H "Authorization: Bearer $TOKEN"
```

## Auditoría

Toda request a un endpoint del API queda en `api_audit_log`:

```sql
SELECT ts, username, method, path, status_code, ip
FROM api_audit_log
ORDER BY id DESC LIMIT 50;
```

Útil para:
- Detectar abuso (mismo user con muchos 403)
- Atribuir cambios (quién creó/modificó qué user)
- Compliance

## Esquema de las tablas API

```sql
CREATE TABLE api_users (
    id            INTEGER PRIMARY KEY,
    username      VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,    -- bcrypt
    role          VARCHAR(20) NOT NULL,     -- 'super_admin' | 'regular'
    is_active     BOOLEAN NOT NULL DEFAULT TRUE,
    created_at    TIMESTAMP WITH TIME ZONE NOT NULL,
    updated_at    TIMESTAMP WITH TIME ZONE NOT NULL
);

CREATE TABLE api_user_permissions (
    user_id       INTEGER NOT NULL REFERENCES api_users(id) ON DELETE CASCADE,
    catalog_name  VARCHAR(120) NOT NULL,
    granted_at    TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (user_id, catalog_name)
);

CREATE TABLE api_audit_log (
    id          INTEGER PRIMARY KEY,
    ts          TIMESTAMP WITH TIME ZONE NOT NULL,
    user_id     INTEGER,
    username    VARCHAR(80),
    method      VARCHAR(10) NOT NULL,
    path        VARCHAR(255) NOT NULL,
    status_code INTEGER NOT NULL,
    ip          VARCHAR(64),
    notes       TEXT
);
```

Generadas idempotentemente por `bootstrap.py` o por el lifespan del FastAPI.

## Deploy

### Docker (extiende el `Dockerfile` base)

```dockerfile
FROM ghcr.io/orlandobcr/co-salud-catalogos:0.1
RUN uv pip install --system -e ".[api,postgres]"

ENV SALUD_API_DB_URL=postgresql+psycopg://user:pass@db/salud
# SALUD_API_JWT_SECRET pasada por secret manager o docker secrets

EXPOSE 8000
CMD ["uvicorn", "sync_catalogos.api.main:app", \
     "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### systemd

```ini
# /etc/systemd/system/salud-api.service
[Unit]
Description=co-salud-catalogos API
After=network.target postgresql.service

[Service]
Type=simple
User=co-salud
Group=co-salud
WorkingDirectory=/opt/co-salud-catalogos
EnvironmentFile=/opt/co-salud-catalogos/.env
ExecStart=/home/co-salud/.local/bin/uv run uvicorn sync_catalogos.api.main:app \
    --host 0.0.0.0 --port 8000 --workers 4
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now salud-api
sudo journalctl -u salud-api -f
```

### Detrás de Nginx / Traefik

```nginx
server {
    listen 443 ssl;
    server_name salud-api.example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Hardening

- **JWT_SECRET fuerte**: `openssl rand -hex 32` (32 bytes mínimo)
- **HTTPS obligatorio** en producción (delegar a Nginx / ALB)
- **CORS restringido**: setear `SALUD_API_CORS_ORIGINS` con la lista exacta de orígenes (no `*`)
- **Rate limiting**: añadir capa frontera (Nginx / Traefik / WAF)
- **DB user con menor privilegio**: SELECT en `salud_*` + ALL en `api_*`
- **Rotación de tokens**: el JWT actual no soporta refresh — los users re-loguean cada 8h. Si se requiere, añadir refresh token (futuro)
- **Backup tabla `api_users`** con la misma frecuencia que el resto de la DB

## Limitaciones conocidas

- Token expirado = re-login (no hay refresh token aún)
- Permisos solo por catálogo (no por kind / área / wildcard) — futuro
- Audit log no rota automáticamente — agregar trigger o cron de DELETE periódico
- Sin reset de password vía email — solo super_admin puede resetear via PATCH
- Sin MFA — futuro

## Próxima lectura

- [Manual de uso del CLI](04-manual-uso.md) — para sincronizar la data que la API consume
- [Despliegue](06-despliegue.md) — operación productiva del sync
- [Pruebas](07-pruebas.md) — validación pre-producción

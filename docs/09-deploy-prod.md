# 9. Deploy de producción — co-health-api.zetgo.io

Documento del deploy actual en `co-health-api.zetgo.io` (149.33.21.108). Sirve como referencia de operación.

## Stack desplegado

| Componente   | Versión       | Configuración                                          |
|--------------|---------------|--------------------------------------------------------|
| OS           | Ubuntu 24.04 LTS (Noble) | x86_64                                       |
| Python       | 3.12.3        | system, venv en `/opt/co-salud-catalogos/.venv`        |
| PostgreSQL   | 16.13         | `salud` DB, user `salud`, listen 127.0.0.1:5432         |
| Nginx        | 1.24.0        | reverse proxy con HTTPS                                |
| Uvicorn      | 0.46          | systemd `co-salud-api`, 2 workers, listen 127.0.0.1:8000 |
| Let's Encrypt| —             | cert auto-renew via certbot timer                      |

## URLs públicas

| URL                                                | Propósito                          |
|----------------------------------------------------|------------------------------------|
| `https://co-health-api.zetgo.io/`                  | Landing con login                  |
| `https://co-health-api.zetgo.io/dashboard`         | Panel autenticado                  |
| `https://co-health-api.zetgo.io/docs`              | Swagger UI dinámico                |
| `https://co-health-api.zetgo.io/redoc`             | ReDoc                              |
| `https://co-health-api.zetgo.io/openapi.json`      | OpenAPI spec (filtrado por user)   |
| `https://co-health-api.zetgo.io/api/v1/auth/login` | POST login → bearer JWT            |
| `https://co-health-api.zetgo.io/api/v1/catalogs`   | GET catálogos                      |
| `https://co-health-api.zetgo.io/api/v1/admin/*`    | super_admin only                   |
| `https://co-health-api.zetgo.io/health`            | Health check (público)             |

## Layout en disco

```
/opt/co-salud-catalogos/         ← repo + venv (owner: cosalud:cosalud)
├── .git/
├── .env                          ← secretos, chmod 600 (gitignored)
├── .venv/                        ← virtualenv Python 3.12
├── sync_catalogos/               ← código
└── ...

/etc/systemd/system/
└── co-salud-api.service          ← unit del API

/etc/nginx/sites-enabled/
└── co-health-api                 ← reverse proxy

/etc/letsencrypt/live/co-health-api.zetgo.io/  ← certs HTTPS

/var/log/nginx/
├── co-health-api.access.log
└── co-health-api.error.log

/root/
├── co-salud-secrets.txt          ← backup de credenciales (chmod 600)
└── backup-pre-noble/             ← backup pre-upgrade Ubuntu
```

## Accesos administrativos

- **SSH**: solo por pubkey (PasswordAuthentication = no en `/etc/ssh/sshd_config.d/00-disable-password.conf`)
- **Postgres**: usuario `salud` (peer/local) — `psql -U salud -h 127.0.0.1 salud`
- **Super_admin API**: ver `/root/co-salud-secrets.txt` (no se commitea, no aparece en logs)

## Operación

### Estado del API

```bash
systemctl status co-salud-api
journalctl -u co-salud-api -f             # logs en vivo
journalctl -u co-salud-api -n 200         # últimas 200 líneas
journalctl -u co-salud-api --since '1 hour ago' --grep ERROR
```

### Restart / reload

```bash
systemctl restart co-salud-api            # cambios en .env o código
systemctl reload nginx                    # cambios en nginx config
```

### Logs nginx

```bash
tail -f /var/log/nginx/co-health-api.access.log
tail -f /var/log/nginx/co-health-api.error.log
```

### Verificar cert HTTPS

```bash
certbot certificates
certbot renew --dry-run
```

Renovación automática vía systemd timer:
```bash
systemctl list-timers | grep certbot
```

### Backup DB

```bash
sudo -u postgres pg_dump salud | gzip > /root/backups/salud-$(date +%F).sql.gz
```

### Sync manual de catálogos

```bash
cd /opt/co-salud-catalogos
sudo -u cosalud bash -c "
    set -a; source /opt/co-salud-catalogos/.env; set +a
    .venv/bin/python -m sync_catalogos.sync \
        --all --kind socrata \
        --db \"\$SALUD_API_DB_URL\" --no-write-json
"
```

### Sync con consentimiento (SISPRO — solo manual, documentado)

```bash
sudo -u cosalud bash -c "
    set -a; source /opt/co-salud-catalogos/.env; set +a
    .venv/bin/python -m sync_catalogos.sync \
        --all --kind sispro_aspx --i-have-permission \
        --db \"\$SALUD_API_DB_URL\" --no-write-json
"
```

## Deploy de updates de código

```bash
cd /opt/co-salud-catalogos
sudo -u cosalud git pull
sudo -u cosalud .venv/bin/pip install -e ".[api,postgres]"   # si cambiaron deps
systemctl restart co-salud-api
```

## Variables de entorno productivas

`/opt/co-salud-catalogos/.env` (chmod 600, owner cosalud:cosalud, gitignored):

```dotenv
SALUD_API_DB_URL=postgresql+psycopg://salud:<password>@127.0.0.1:5432/salud
SALUD_API_JWT_SECRET=<32-byte-hex>
SALUD_API_BIND_HOST=127.0.0.1
SALUD_API_BIND_PORT=8000
SALUD_API_CORS_ORIGINS=https://co-health-api.zetgo.io
```

## Nginx config (referencia)

`/etc/nginx/sites-enabled/co-health-api`:
```nginx
server {
    listen 80;
    listen [::]:80;
    server_name co-health-api.zetgo.io;

    if ($host = co-health-api.zetgo.io) {
        return 301 https://$host$request_uri;
    }
    return 404;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name co-health-api.zetgo.io;

    ssl_certificate /etc/letsencrypt/live/co-health-api.zetgo.io/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/co-health-api.zetgo.io/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    client_max_body_size 16M;
    client_body_timeout 600s;
    proxy_read_timeout 600s;
    proxy_connect_timeout 60s;

    access_log /var/log/nginx/co-health-api.access.log;
    error_log  /var/log/nginx/co-health-api.error.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
    }
}
```

(El bloque HTTPS lo creó certbot automáticamente al correr `certbot --nginx`.)

## systemd unit (referencia)

`/etc/systemd/system/co-salud-api.service`:
```ini
[Unit]
Description=co-salud-catalogos REST API (uvicorn)
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=simple
User=cosalud
Group=cosalud
WorkingDirectory=/opt/co-salud-catalogos
EnvironmentFile=/opt/co-salud-catalogos/.env
ExecStart=/opt/co-salud-catalogos/.venv/bin/uvicorn sync_catalogos.api.main:app \
    --host 127.0.0.1 --port 8000 --workers 2 \
    --proxy-headers --forwarded-allow-ips '*'
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ReadWritePaths=/opt/co-salud-catalogos
ProtectHome=true

[Install]
WantedBy=multi-user.target
```

## Hardening aplicado

- ✅ HTTPS obligatorio (redirect 80→443)
- ✅ Cert válido auto-renovado
- ✅ SSH solo por pubkey (`PasswordAuthentication no`, `PermitRootLogin prohibit-password`)
- ✅ Postgres bind localhost (no expone 5432 externamente)
- ✅ Uvicorn bind localhost (nginx es el único expuesto)
- ✅ Servicio corre con user no-root (`cosalud`)
- ✅ systemd hardening: `NoNewPrivileges`, `PrivateTmp`, `ProtectSystem=strict`, `ProtectHome`, `ReadWritePaths` solo al directorio del proyecto
- ✅ JWT_SECRET 32 bytes random
- ✅ Password hashing bcrypt cost 12
- ✅ `.env` chmod 600 propiedad de `cosalud`
- ✅ CORS limitado al dominio de producción

## Cron pendiente (a configurar bajo supervisión)

Recomendado (NO automatizado todavía):
```cron
# Lunes 03:00 UTC — REPS Habilitación (semanal)
0 3 * * 1 cd /opt/co-salud-catalogos && sudo -u cosalud bash -c 'set -a; source .env; set +a; .venv/bin/python -m sync_catalogos.sync --all --kind reps_export --db "$SALUD_API_DB_URL" --no-write-json' >> /var/log/co-salud-catalogos/sync.log 2>&1

# Lunes 04:00 UTC — Datos Abiertos (semanal)
0 4 * * 1 cd /opt/co-salud-catalogos && sudo -u cosalud bash -c 'set -a; source .env; set +a; .venv/bin/python -m sync_catalogos.sync --all --kind socrata --db "$SALUD_API_DB_URL" --no-write-json' >> /var/log/co-salud-catalogos/sync.log 2>&1

# SISPRO: NUNCA en cron — solo manual con --i-have-permission documentado
```

## Smoke tests rápidos

```bash
# health (público)
curl https://co-health-api.zetgo.io/health

# login
TOKEN=$(curl -s -X POST https://co-health-api.zetgo.io/api/v1/auth/login \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"<la-pass>"}' | jq -r .access_token)

# catálogos
curl -s https://co-health-api.zetgo.io/api/v1/catalogs \
    -H "Authorization: Bearer $TOKEN" | jq

# entries
curl -s "https://co-health-api.zetgo.io/api/v1/catalogs/divipola_municipios/entries?q=MEDELL&limit=5" \
    -H "Authorization: Bearer $TOKEN" | jq

# Swagger en browser (con bearer set en "Authorize")
open https://co-health-api.zetgo.io/docs
```

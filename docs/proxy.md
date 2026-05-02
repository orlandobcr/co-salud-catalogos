# Pool de proxies

El sincronizador soporta un pool de proxies opcional con **fallback automático a conexión directa** si el proxy falla o no está configurado.

## Diseño

- **Paramétrico**: si nada está seteado, el pool queda inactivo y todo va directo (mismo comportamiento que sin proxy).
- **Pluggable provider**: tres fuentes soportadas via env (en orden de prioridad).
- **Sticky por host**: la misma corrida reusa el mismo proxy para mantener cookies de sesión ASP.NET (REPS / SISPRO).
- **Health tracking**: tras N fallos consecutivos, una IP entra en cooldown (default 5 min).
- **Fallback automático**: si todos los proxies del pool fallan en una request, se reintenta directo. Si la directa también falla, se propaga el error.

## Providers soportados

### 1. Lista plana (`PROXY_LIST`)

CSV de URLs en una variable. Ideal para listas mantenidas a mano o pegadas desde otro sistema.

```bash
export PROXY_ENABLED=true
export PROXY_LIST="http://user:pass@1.2.3.4:8000,socks5://user:pass@5.6.7.8:1080"
```

### 2. Endpoint propio (`PROXY_LIST_URL`)

Apunta a un endpoint HTTP que devuelve JSON o texto plano. Útil para integrar con cualquier proveedor (BrightData, IPRoyal, ScraperAPI, Smartproxy, listas internas, etc.).

```bash
export PROXY_ENABLED=true
export PROXY_LIST_URL="https://my-proxy-broker.example/list?token=..."
```

Formato JSON aceptado:
```json
["http://1.2.3.4:8000", "socks5://5.6.7.8:1080"]
```
o
```json
{"proxies": [{"host":"1.2.3.4","port":8000,"user":"u","password":"p","protocol":"http"}]}
```

Formato texto: una URL por línea (líneas con `#` ignoradas).

### 3. 2captcha proxy network (`TWOCAPTCHA_API_KEY`)

[2Captcha Residential Proxy](https://2captcha.com/proxy) — ~220 países, IPs residenciales, autenticación por whitelist de IP del cliente.

```bash
export PROXY_ENABLED=true
export TWOCAPTCHA_API_KEY=...
export PROXY_COUNTRY=co               # opcional, default mix
export PROXY_PROTOCOL=http            # http | https | socks5
export PROXY_POOL_SIZE=10             # 1..2000
```

**Setup obligatorio antes de usar:**
1. Whitelist tu IP pública en https://2captcha.com/setting/ip-whitelist
2. Verifica con `curl 'https://api.2captcha.com/proxy?key=$TWOCAPTCHA_API_KEY'` — `ip_white` debe contener tu IP
3. Si está vacía, el provider devuelve [] y el sync va a directo (no falla)

**Conocido**: los proxies HTTP de 2captcha pueden dar `SSL UNEXPECTED_EOF` para targets HTTPS. Si los catálogos a sincronizar son HTTPS (Datos Abiertos, REPS, SISPRO lo son), probar con `PROXY_PROTOCOL=socks5` que sí soporta tunneling.

## Variables de configuración

| Variable | Default | Descripción |
|----------|---------|-------------|
| `PROXY_ENABLED` | `false` | Activa el pool. Si `false`, todo va directo sin tocar el provider. |
| `PROXY_USE_FOR_KINDS` | (auto) | CSV de kinds que usan proxy. Si no se setea, solo `sispro_aspx`. Vacío explícito = ninguno. |
| `PROXY_LIST` | — | Lista CSV de URLs (provider 1) |
| `PROXY_LIST_URL` | — | Endpoint JSON/texto (provider 2) |
| `TWOCAPTCHA_API_KEY` | — | API key 2captcha (provider 3) |
| `PROXY_COUNTRY` | mix | ISO 2-letter (co, us, mx, ...) — solo aplica a 2captcha |
| `PROXY_PROTOCOL` | (todos) | http \| https \| socks5 — vacío = los 3, mejor fallback |
| `PROXY_POOL_SIZE` | 10 | Cantidad de IPs a generar (2captcha, 1..2000) |
| `PROXY_REFRESH_MINUTES` | 30 | Cada cuánto re-pregunta al provider |
| `PROXY_FAIL_THRESHOLD` | 3 | Fallos consecutivos antes de cooldown |
| `PROXY_COOLDOWN_SECONDS` | 300 | Cuánto descansa una IP unhealthy |
| `PROXY_MAX_ATTEMPTS` | 6 | Cuántos proxies probar antes de fallback a directo |

## ¿Qué fuentes usan proxy?

Por **default** solo SISPRO usa el pool. Las otras dos van directo siempre.

| Kind | Default `use_proxy` | Razón |
|------|---------------------|-------|
| `socrata` | **false** | API REST pública con app token gratis (`SALUD_SOCRATA_APP_TOKEN`) sube rate de 1k/h a 100k/h |
| `reps_export` | **false** | Portal público con login `invitado/invitado`, sin restricción |
| `sispro_aspx` | **true** | `robots.txt: Disallow: /` + sync masivo de 297+ tablas |
| `manual` | false | n/a |

Override con `PROXY_USE_FOR_KINDS` (CSV):
```bash
PROXY_USE_FOR_KINDS=sispro_aspx,reps_export   # añadir REPS al proxy
PROXY_USE_FOR_KINDS=                          # ninguno (todo directo)
```

Nota: aunque un kind pida proxy, si `PROXY_ENABLED=false` o no hay provider configurado, el HttpClient va directo igual (sin overhead).

## Comportamiento esperado

| Configuración | Comportamiento |
|---------------|---------------|
| Sin variables proxy | Todo directo (modo legacy) |
| `PROXY_ENABLED=false` | Todo directo aunque haya provider configurado |
| `PROXY_ENABLED=true` + provider configurado + healthy | Usa proxy para todas las requests |
| `PROXY_ENABLED=true` + provider configurado + todos unhealthy | Fallback automático a directo |
| `PROXY_ENABLED=true` + provider mal configurado | Provider devuelve [] → fallback a directo |
| Proxy timeout / connect error | Marca proxy como failed, reintenta con otro, eventualmente directo |
| 4xx/5xx HTTP del target | NO es culpa del proxy → no rota, propaga error |

## Logs útiles

El módulo loguea via `logging` con nombre `sync_catalogos.proxy`. Eventos:
- `proxy.refreshed` — pool re-cargado, `count=N`
- `proxy.refresh_empty` — provider devolvió 0 proxies
- `proxy.attempt_failed` — un proxy falló, intentando el siguiente
- `proxy.unhealthy` — un proxy entró en cooldown
- `proxy.fallback_direct` — agotados los intentos de proxy, yendo directo
- `proxy.2captcha.no_whitelist_ips` — la cuenta 2captcha no tiene IPs whitelisted

Para ver:
```bash
PYTHONLOGLEVEL=INFO python -m sync_catalogos.sync --catalog reps_sedes
```

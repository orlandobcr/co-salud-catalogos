# 3. Funcionamiento

## Modelo mental

El sistema es un **pipeline determinista por catálogo**:

```
discover → fetch → parse → infer schema → persist (JSON ± DB) → report
```

Cada catálogo en el `REGISTRY` (`sync_catalogos/sources.py`) declara:
- `name` — id lógico
- `kind` — `socrata` | `sispro_aspx` | `reps_export` | `manual`
- `output_path` — ruta relativa bajo `catalogos_co/`
- credenciales / IDs específicos del kind (`socrata_dataset_id`, `sispro_code`, `reps_endpoint`)
- `requires_explicit_consent` — `True` para SISPRO

El CLI `sync.py` toma este registry y dispatcha al cliente correcto según el `kind`.

---

## Flujos por kind

### Socrata (datos.gov.co)

```
1. URL = https://www.datos.gov.co/resource/{dataset_id}.json
2. Loop:
     GET URL?$limit=50000&$offset=N&$order=:id
     entries.extend(page)
     if len(page) < 50000: break
     N += 50000
3. metadata_view(dataset_id) → leer rowsUpdatedAt → version ISO-8601
```

Notas:
- `$order=:id` garantiza paginación estable sin duplicados.
- `SALUD_SOCRATA_APP_TOKEN` sube el rate limit de ~1k/h a ~100k/h.
- Sin proxy por default (no aporta valor; rate limit se resuelve con token).

### SISPRO (web.sispro.gov.co)

```
1. URL = https://web.sispro.gov.co/...?Code=<X>
2. GET → captura __VIEWSTATE, __VIEWSTATEGENERATOR, __EVENTVALIDATION
3. POST con __EVENTTARGET=ddlPageSize, value=2000 (resize grid)
4. Lee Items NN del HTML → total esperado
5. Loop páginas 2..ceil(total/2000):
     POST con __EVENTTARGET=grvTablaReferencia, __EVENTARGUMENT=Page$N
     parse <table id="grvTablaReferencia"> → rows
6. version = timestamp de sync (no hay version en SISPRO)
```

Notas:
- Requiere `--i-have-permission` (robots.txt = `Disallow: /`).
- Algunos catálogos grandes (CIE10/CUPS/IUM) tienen **leve duplicación de bordes de página** — backlog conocido.
- Por default usa proxy si `PROXY_ENABLED=true` y `PROXY_USE_FOR_KINDS` lo incluye.

### REPS (prestadores.minsalud.gov.co)

```
1. login(): POST /habilitacion/work.aspx con tbid_usuario=invitado, tbcontrasena=invitado
   → cookie ASP.NET_SessionId
2. GET /habilitacion/consultas/<endpoint>.aspx → HTML del form
3. POST search (body mínimo: __VIEWSTATE + ibBuscarFtr.x/y)
   → HTML con grid + state nuevo
4. POST ibText (botón "Exportar a Texto") con tbSeparator=";"
   → CSV completo (Content-Type: application/vnd.ms-notepad; charset=iso-8859-15)
5. Decode iso-8859-15, normalize \r → \n, csv.DictReader, separator=";"
6. version = timestamp de sync
```

Notas:
- El "body mínimo" es crítico: si se envían dropdowns, ASP.NET event validation rechaza con 500 (los valores no fueron registrados en el render inicial).
- El export CSV usa `\r` (Mac classic) como terminador. Se normaliza a `\n` antes de csv.DictReader.
- Volumen alto (`reps_servicios.aspx` = 228k filas, ~155 MB CSV). Tarda ~95 s.

### Manual

```
No hace nada — entradas marcadas como `kind="manual"` están en disco curadas
a mano (ej. apellidos colombianos, stop-list clínico). El sync las salta.
```

---

## Inferencia de tipos

(Detalle en `db_schema.py`.)

Para cada columna del catálogo, sobre los valores no-vacíos:

| Heurística                                      | Tipo SQL                |
|-------------------------------------------------|-------------------------|
| Todos parsean como `int` (≤19 dígitos)          | `BIGINT`                |
| Todos parsean como `float` (acepta `,` decimal) | `DOUBLE PRECISION`      |
| Todos en `{si, no, sí, true, false, y, n, 0, 1}` con ≥2 tokens distintos y NO todos enteros | `BOOLEAN` |
| Todos coinciden con patrón fecha:               | `DATE`                  |
|   `YYYY-MM-DD`, `DD/MM/YYYY`, `YYYYMMDD`, ISO   |                         |
| Resto, `max_len ≤ 50` (con +25% buffer)         | `VARCHAR(50)`           |
| `max_len ≤ 100`                                 | `VARCHAR(100)`          |
| `max_len ≤ 255`                                 | `VARCHAR(255)`          |
| `max_len ≤ 1000`                                | `VARCHAR(1000)`         |
| `max_len ≤ 4000`                                | `VARCHAR(4000)`         |
| `max_len > 4000`                                | `TEXT`                  |

**Excepciones**:
- Si todos son enteros pero algunos llevan `0` al frente (ej. `05` Antioquia, `0500100019` cod habilitación), se preserva como `VARCHAR` para no perder el padding.
- Si todos parsean como float, `BIGINT` ya hizo el corto antes; solo queda `DOUBLE` para decimales reales.
- El `max_len` se calcula sobre **TODAS** las filas, no una muestra (evita truncar en bulk insert).
- El buffer +25% absorbe valores levemente más largos en sync futuros.

### Sanitización de nombres de columna

| Original                              | Sanitizado                    |
|---------------------------------------|-------------------------------|
| `Categorías Médicas`                  | `categorias_medicas`          |
| `Municipio PDET`                      | `municipio_pdet`              |
| `Municipio PNSR antes 2023`           | `municipio_pnsr_antes_2023`   |
| `Extra_I:TipoRegimen`                 | `extra_i_tiporegimen`         |
| `Modalidad Extramural Unidad Móvil`   | `modalidad_extramural_unidad_movil` |
| `2023_value`                          | `c_2023_value` (no empieza con dígito) |
| `select`                              | `select_` (palabra reservada) |

Algoritmo:
1. NFKD ASCII fold (acentos → sin tilde, ñ → n)
2. Lowercase
3. Cualquier no-`[a-z0-9_]` → `_`
4. Colapsa `_` repetidos, trim
5. Truncar a 63 chars (límite Postgres)
6. Prefijo `c_` si empieza con dígito
7. Sufijo `_` si es palabra reservada SQL
8. Dedup con `_2`, `_3` si dos originales colapsan

**Los valores siempre preservan UTF-8**. Solo los nombres de tabla / columna se sanean.

### Coerción de valores

`coerce_value(raw, sql_type_name)` transforma cada valor del JSON al tipo destino:

- `BIGINT`: `int(s)` o `None` si no parsea
- `DOUBLE PRECISION`: `float(s.replace(",", "."))` o `None`
- `BOOLEAN`: `s.lower() in {si, sí, true, y, yes, 1, t}`
- `DATE`: prueba cada patrón → `datetime.strptime(...).date()`
- `VARCHAR/TEXT`: preserva el string tal cual (UTF-8)

`None` se inserta como `NULL` en SQL / `null` en Mongo.

---

## Idempotencia

Cada sync es **idempotente**: correr dos veces seguidas produce el mismo estado.

- **JSON**: `write_catalog()` usa `tempfile + atomic rename` → nunca queda parcial.
- **SQL**: cada `write_catalog()` corre `DELETE FROM <tabla>` + `INSERT bulk` dentro de una transacción. Si la transacción falla, la tabla queda igual a antes.
- **Mongo**: `delete_many({})` + `bulk_write` por colección. No es transaccional sin replica set, pero es secuencial — un fallo deja la colección vacía y el siguiente sync la repuebla.
- **Metadata**: `salud_catalog_metadata` se upserta (delete + insert) por `name`.

El `sha256` en metadata permite detectar si un catálogo cambió entre dos syncs (distintos hashes = datos cambiaron).

---

## Comportamiento ante fallos

### Fallo del scraper (red, parse error, format change)

- El `try/except` en `sync_one()` captura → registra `result["error"]` → continúa con el siguiente catálogo.
- Sin parar el batch. El `--all` siempre llega al final.
- Exit code distinto de 0 si hubo cualquier error → cron lo detecta.

### Fallo del proxy

(Solo aplica a kinds con `use_proxy=True`, default solo SISPRO.)

```
Request → proxy_sticky → falla → reintenta con otro proxy → falla
       → ... hasta `max_attempts` proxies, alternando protocolos (HTTP, HTTPS, SOCKS5)
       → fallback automático a directo
       → si directo falla → propaga el error
```

Health tracking: tras 3 fallos consecutivos un proxy entra en cooldown 5 min. Reduce overhead en syncs largos.

### Fallo del DB sink

- Si `--db` está activo y la conexión falla, se loguea `result["db_error"]` pero el JSON sí se escribe (si `--no-write-json` no está activo).
- Si solo `--db` (sin JSON) y falla → `result["error"]`.
- El sync individual no contamina otros catálogos.

### Fallo de SISPRO sin consentimiento

- Si `requires_explicit_consent=True` y no hay `--i-have-permission`, el catálogo se marca `skipped` con razón. No es error.

---

## Scheduling recomendado

| Catálogos              | Frecuencia recomendada | Por qué                                                  |
|------------------------|------------------------|----------------------------------------------------------|
| REPS (todos los 6)     | semanal                | Habilitaciones / sanciones cambian semanalmente          |
| DIVIPOLA, postales     | trimestral             | Cambios estructurales raros                              |
| Vías INVIAS            | semestral / anual      | Red vial nacional                                        |
| CIE-10                 | anual                  | Versión vigente hasta 2027                               |
| CUPS                   | anual                  | Actualizaciones formales MinSalud                        |
| IUM, ATC, CUMs         | trimestral             | Medicamentos cambian más seguido                         |
| Resto SISPRO           | trimestral             | Tablas de referencia administrativas                     |
| EAPB                   | mensual                | Régimen / estado de EPS puede cambiar                    |

Ejemplo crontab:
```cron
# Lunes 03:00 — semanal: REPS + Datos Abiertos
0 3 * * 1 cd /opt/co-salud-catalogos && uv run python -m sync_catalogos.sync --all --kind socrata
30 3 * * 1 cd /opt/co-salud-catalogos && uv run python -m sync_catalogos.sync --all --kind reps_export

# 1er domingo del trimestre — SISPRO con consentimiento operativo (manual)
# NO automatizar SISPRO. Documentar cada ejecución en bitácora.
```

Detalle en [Despliegue §6](06-despliegue.md#cron).

---

## Observabilidad

### Output del CLI

Modo humano (default):
```
Sincronizados: 12  con error: 0  saltados: 0
  ✓ divipola_municipios          1122   1.0s  → /path/...
  ✓ reps_sedes                  76561  17.3s  → /path/...
  ✓ reps_servicios             228293 161.4s  → /path/...
  ...
```

Modo JSON (para pipelines):
```bash
python -m sync_catalogos.sync --all --json > sync_report.json
```

### Logs

Logger root: `sync_catalogos.*`. Eventos clave:

| Logger                          | Evento                                          |
|---------------------------------|-------------------------------------------------|
| `sync_catalogos.proxy`          | `proxy.refreshed`, `proxy.attempt_failed`, `proxy.fallback_direct`, `proxy.unhealthy` |
| `sync_catalogos.proxy.2captcha` | `2captcha.no_whitelist_ips`, `2captcha.invalid_ip_port` |
| `sync_catalogos.sispro`         | `sispro.empty_page`                             |

Activar con:
```bash
PYTHONLOGLEVEL=INFO python -m sync_catalogos.sync ...
```

### Diagnóstico del proxy

```bash
python -m sync_catalogos.proxy_check
```

Reporta config env, defaults por kind, balance/whitelist 2captcha, pool refrescado, distribución por protocolo, test de conectividad por proxy.

---

## Próxima lectura

- [Manual de uso](04-manual-uso.md) — comandos paso a paso
- [Deep technical](05-deep-technical.md) — para extender el sistema

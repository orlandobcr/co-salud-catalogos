# 5. Deep technical

Para devs que vayan a tocar código, añadir scrapers, sinks o providers de proxy.

## Estructura del paquete

```
sync_catalogos/
├── __init__.py             docstring + nada más exportado
├── _envfile.py             load .env sin python-dotenv
├── schema.py               dataclasses CatalogFile / CatalogMetadata
├── io.py                   write_catalog (atomic) + hash_entries
├── sources.py              REGISTRY: 319 CatalogSource declarados
├── socrata.py              cliente Datos Abiertos (datos.gov.co)
├── sispro.py               cliente SISPRO (ASP.NET WebForms scraper)
├── reps.py                 cliente REPS (login + ibText export)
├── proxy.py                ProxyPool, HttpClient, providers
├── proxy_check.py          CLI de diagnóstico
├── db_schema.py            inferencia de tipos + sanitization
├── db.py                   SqlSink + MongoSink + factory
└── sync.py                 CLI principal
```

Cada archivo es <500 LOC excepto `sources.py` (3300 LOC, casi todo data del REGISTRY).

## Modelo (`schema.py`)

```python
@dataclass
class CatalogMetadata:
    name: str                    # short id (e.g. "divipola_municipios")
    description: str = ""
    source: SourceKind = "manual"  # socrata | sispro_aspx | reps_export | manual
    source_url: str = ""
    source_id: str | None = None # dataset_id Socrata | code SISPRO | endpoint REPS
    version: str | None = None
    license: str = ""
    row_count: int | None = None
    last_synced: str | None = None  # ISO 8601 UTC
    sha256: str | None = None    # hash de las entries serializadas
    notes: str = ""

@dataclass
class CatalogFile:
    metadata: CatalogMetadata
    entries: list[Any] = field(default_factory=list)
```

`CatalogFile.from_dict()` reconstruye desde el JSON; `to_dict()` serializa.

## Registry (`sources.py`)

```python
@dataclass(frozen=True)
class CatalogSource:
    name: str
    kind: SourceKind
    output_path: Path
    description: str
    license: str = ""
    schedule_hint: str = "monthly"
    notes: str = ""
    requires_explicit_consent: bool = False
    consent_reason: str = ""
    # Específicos por kind:
    socrata_dataset_id: str | None = None
    socrata_extra_query: str | None = None
    sispro_code: str | None = None
    sispro_page_size: int = 2000
    reps_endpoint: str = ""
    manual_source_url: str = ""

REGISTRY: list[CatalogSource] = [
    CatalogSource(name="reps_sedes", kind="reps_export", reps_endpoint="sedes_reps.aspx", ...),
    ...
]
```

Para agregar un catálogo:

1. Si es Socrata, conoce su `dataset_id` (en la URL: `https://www.datos.gov.co/d/<id>`).
2. Si es SISPRO, conoce su `Code` (probar con `proxy_check.py` o `curl`).
3. Si es REPS, conoce su endpoint (`<algo>_reps.aspx`).
4. Append una `CatalogSource(...)` al `REGISTRY`.
5. Probar con `python -m sync_catalogos.sync --catalog <name>`.

## Scrapers (kinds existentes)

### `socrata.py`

API SODA pública. Paginación con `$limit`/`$offset`/`$order=:id`.

```python
def fetch_all(dataset_id, *, where=None, page_size=50_000, progress_cb=None, use_proxy=False):
    cli = make_http_client(SOCRATA_HOST, ..., use_proxy=use_proxy)
    while True:
        r = cli.get(f"{SOCRATA_BASE}/{dataset_id}.json",
                   params={"$limit": page_size, "$offset": offset, "$order": ":id"})
        page = r.json()
        if not page: break
        out.extend(page)
        if len(page) < page_size: break
        offset += page_size
    return out
```

Headers: `X-App-Token` opcional desde `SALUD_SOCRATA_APP_TOKEN`.

### `sispro.py`

Scraper ASP.NET WebForms. Requiere mantener `__VIEWSTATE`/`__EVENTVALIDATION` entre requests.

```python
GRID_ID = "ctl00_cntContenido_grvTablaReferencia"
PAGE_SIZE_NAME = "ctl00$cntContenido$dpggrvTablaReferencia$ddlPageSize"

# 1. GET inicial → captura state
# 2. POST __EVENTTARGET=PAGE_SIZE_NAME, value=2000 → resize grid
# 3. Lee Items NN del HTML → total
# 4. Por cada página 2..ceil(total/2000):
#    POST __EVENTTARGET=GRID_NAME, __EVENTARGUMENT=Page$N
```

Parser usa `lxml.html.fromstring` + xpath para extraer `__VIEWSTATE` y `<table id="...">`.

### `reps.py`

Portal con guest login + botón oficial "Exportar a Texto".

```python
GUEST_USER = "invitado"
GUEST_PASS = "invitado"

def fetch_export(endpoint, *, progress_cb=None, use_proxy=False):
    c = _client(use_proxy=use_proxy)   # HttpClient con cookies persistentes
    login(c)                            # → ASP.NET_SessionId cookie
    r = c.get(URL)
    html = _search(c, url, html)        # POST search con body MÍNIMO
    raw = _export(c, url, html)         # POST ibText → CSV bytes (iso-8859-15)
    return _parse_csv(raw, ...)
```

**Truco crítico** (descubierto durante desarrollo): el body POST debe ser **mínimo** (solo `__VIEWSTATE` + `_ctl0:ibBuscarFtr.x/y`). Si se incluyen los `<select>` con sus valores, ASP.NET event validation rechaza con HTTP 500 ("Invalid postback or callback argument").

### Como añadir un nuevo source

1. Crear `sync_catalogos/<source>.py` con función `fetch_all(...)` o `fetch_export(...)` que devuelve `list[dict]`.
2. Añadir el nuevo `SourceKind` literal en `schema.py`:
   ```python
   SourceKind = Literal["socrata", "sispro_aspx", "reps_export", "manual", "mi_nueva_fuente"]
   ```
3. Añadir campos específicos a `CatalogSource` en `sources.py` si los necesita.
4. Añadir el dispatch en `sync_one()` de `sync.py`:
   ```python
   elif src.kind == "mi_nueva_fuente":
       entries = mi_nueva_fuente.fetch_all(src.mi_param, use_proxy=use_proxy)
       version = ...
   ```
5. Actualizar `_DEFAULT_USE_PROXY_BY_KIND` en `proxy.py` con el default sensato.
6. Tests: `python -m sync_catalogos.sync --catalog <nombre>`.

---

## Inferencia de schema (`db_schema.py`)

### Pipeline

```
entries (list[dict])
    │
    ▼
Recolectar TODAS las keys (preservando orden de aparición, sample 200 entries)
    │
    ▼
dedupe_names(originals) → {original: sql_name}   # ASCII fold + sanitize + dedup
    │
    ▼
Para cada (original, sql_name):
    │
    ▼
infer_column_type(values) → (sql_type_name, max_observed, nullable)
    │   ├─ check int → BIGINT
    │   ├─ check float → DOUBLE PRECISION
    │   ├─ check bool → BOOLEAN
    │   ├─ check date → DATE
    │   └─ default → VARCHAR(N) / TEXT con buffer +25%
    │
    ▼
ColumnSpec(name, original, sql_type_name, nullable, max_observed, samples)
```

### `sanitize_identifier()` paso a paso

```python
"Categorías Médicas"
  → ascii_fold → "Categorias Medicas"
  → lower → "categorias medicas"
  → sub r'[^a-z0-9_]+' → "categorias_medicas"
  → sub r'_+' → "categorias_medicas"
  → strip("_") → "categorias_medicas"
  → ¿reserved? No
  → ¿len > 63? No
  → "categorias_medicas"
```

### Casos límite

| Original                  | Resultado     | Razón                                              |
|---------------------------|---------------|----------------------------------------------------|
| `""`                      | `col`         | fallback                                           |
| `"123 Foo"`               | `c_123_foo`   | empieza con dígito → prefijo `c_`                  |
| `"select"`                | `select_`     | reserved SQL → sufijo `_`                          |
| `"a" * 100`               | (truncado 63) | límite Postgres                                    |
| dos `"foo"` y `"foo "`    | `foo`, `foo_2`| dedup automático                                   |
| `"FOO"` y `"foo"`         | ambos `foo`, segundo → `foo_2` | colapsan al sanitizar           |

### `coerce_value()` cast por tipo

```python
def coerce_value(v, sql_type):
    if v is None or v == "" or (isinstance(v, str) and v.strip() == ""):
        return None
    s = str(v).strip()
    if sql_type == "BIGINT":      return int(s)
    if sql_type == "DOUBLE PRECISION": return float(s.replace(",", "."))
    if sql_type == "BOOLEAN":     return s.lower() in {"si","sí","true","y","yes","1","t"}
    if sql_type == "DATE":        # try patterns
        for pat, fmt in _DATE_PATTERNS:
            if pat.match(s):
                return datetime.strptime(s, fmt).date() if fmt != "iso" else datetime.fromisoformat(s).date()
    return s   # VARCHAR/TEXT preserva string original
```

### Cómo extender la inferencia

Para añadir un nuevo tipo (ej. `UUID`, `JSON`, `DECIMAL(p,s)`):

1. Añadir checker en `infer_column_type()`:
   ```python
   _UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.I)
   if all(_UUID_RE.match(s) for s in str_values):
       return ("UUID", max_len, nullable)
   ```
2. Añadir `coerce_value` rama:
   ```python
   if sql_type == "UUID":
       return uuid.UUID(s)
   ```
3. Añadir mapeo en `_sql_type_for()` de `db.py`:
   ```python
   if name == "UUID":
       return UUID(as_uuid=True)   # postgresql.UUID
   ```
4. Para Mongo, agregar conversión en `to_bson()` si necesita.

---

## Sinks (`db.py`)

### `SqlSink`

Lazy table creation. Cada catálogo crea su tabla en su primer `write_catalog()`:

```python
def _build_catalog_table(self, catalog_name, schema):
    table_name = sanitize_table_name(catalog_name)   # salud_<name>
    if table_name in self._tables:
        return self._tables[table_name], table_name
    md = MetaData()
    cols = [Column("_idx", Integer, primary_key=True)]
    for spec in schema:
        cols.append(Column(spec.name, _sql_type_for(spec), nullable=spec.nullable))
    table = Table(table_name, md, *cols)
    self._tables[table_name] = table
    return table, table_name

def write_catalog(self, catalog, *, batch_size=1000):
    schema = infer_schema(catalog.entries)
    table, table_name = self._build_catalog_table(m.name, schema)
    table.create(self.engine, checkfirst=True)   # idempotent DDL

    with self.engine.begin() as conn:
        # Upsert metadata
        conn.execute(delete(self.t_meta).where(self.t_meta.c.name == m.name))
        conn.execute(insert(self.t_meta).values(**meta_row))

        # Replace entries: delete + bulk insert
        conn.execute(delete(table))
        rows = [build_row(i, e, schema) for i, e in enumerate(entries)]
        for chunk in chunks_of(rows, batch_size):
            conn.execute(insert(table), chunk)
```

Caché de `Table` objects: una vez construido, no se regenera (mismo SqlSink mantiene el cache para múltiples `write_catalog`).

### `MongoSink`

Mismo modelo, pero con `bulk_write([InsertOne(doc)])`:

```python
def write_catalog(self, catalog, *, batch_size=1000):
    schema = infer_schema(catalog.entries)
    col, col_name = self._collection_for(m.name)   # crea índice _idx unique

    self.col_meta.replace_one({"name": m.name}, meta_doc, upsert=True)
    col.delete_many({})                             # replace strategy

    ops = [InsertOne({"_idx": i, **{spec.name: to_bson(coerce_value(...)) for spec in schema}})
           for i, e in enumerate(entries)]
    for chunk in chunks_of(ops, batch_size):
        col.bulk_write(chunk, ordered=False)
```

`to_bson()` promueve `date` → `datetime` (BSON no soporta bare date).

### Como añadir un nuevo sink

1. Crear clase con métodos `ensure_schema()`, `write_catalog(cat)`, `close()`:
   ```python
   class ClickHouseSink:
       def __init__(self, url): ...
       def ensure_schema(self): ...
       def write_catalog(self, catalog: CatalogFile): ...
       def close(self): ...
   ```
2. Update `make_sink(url)` factory:
   ```python
   if scheme.startswith("clickhouse"):
       return ClickHouseSink(url)
   ```
3. Añadir extras opcionales en `pyproject.toml`:
   ```toml
   [project.optional-dependencies]
   clickhouse = ["clickhouse-driver>=0.2"]
   ```

---

## Proxy (`proxy.py`)

### Componentes

```
ProxyConfig (dataclass)        Configuración leída de env
ProxyEntry (dataclass)         Una IP del pool con health tracking
ProxyPool                      Pool global, sticky por host, refresh periódico
ProxyProvider (Protocol)       Interfaz pluggable
    StaticProvider             PROXY_LIST CSV
    HttpProvider               PROXY_LIST_URL endpoint propio
    TwoCaptchaProvider         2captcha residential network API
HttpClient                     Façade sobre httpx con retry + fallback
make_http_client(host, ...)    Punto de entrada para scrapers
should_use_proxy_for_kind(k)   Decide si un kind usa pool
```

### Flujo de una request con proxy

```
HttpClient.request(method, url):
    if direct_only:
        return _execute(None, ...)

    # 1. Sticky: usa el mismo proxy para este host (cookies)
    sticky = pool.get_for(target_host)
    if sticky:
        try:
            return _execute(sticky, ...)
        except _PROXY_ERROR_TYPES:
            pool.report_failure(sticky)
            pool.clear_stickiness(target_host)
            track failed protocol

    # 2. Resto del pool, ordenado por diversidad de protocolo
    healthy = pool.healthy_proxies(exclude=attempted)
    ordered = _order_by_protocol_diversity(healthy, failed_protocols)
    for proxy in ordered[:max_attempts]:
        try:
            return _execute(proxy, ...)
        except _PROXY_ERROR_TYPES:
            pool.report_failure(proxy)
            track failed protocol

    # 3. Fallback a directo
    return _execute(None, ...)
```

### Como añadir un nuevo provider

```python
class MiProvider:
    def fetch(self) -> list[str]:
        # devuelve lista de URLs http://, https://, socks5://
        return [...]

# Y registrarlo en _make_provider() según prioridad:
def _make_provider() -> ProxyProvider | None:
    ...
    if os.environ.get("MI_API_KEY"):
        return MiProvider(os.environ["MI_API_KEY"])
    ...
```

---

## CLI (`sync.py`)

```python
def main(argv):
    ap = argparse.ArgumentParser(...)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--catalog")
    g.add_argument("--all", action="store_true")
    g.add_argument("--list", action="store_true")
    ap.add_argument("--kind", choices=...)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--i-have-permission", dest="consent", ...)
    ap.add_argument("--db", help="DB URL")
    ap.add_argument("--no-write-json", ...)
    args = ap.parse_args(argv)

    if args.list: return _list()

    db_sink = make_sink(args.db) if args.db else None
    if db_sink: db_sink.ensure_schema()

    results = sync_one(...) if args.catalog else sync_all(...)

    if args.json: print(json.dumps(results, ensure_ascii=False, indent=2))
    else: print_summary(results)

    if db_sink: db_sink.close()
    return 0 if all("error" not in r for r in results) else 1
```

### Como añadir un flag CLI

1. `ap.add_argument("--mi-flag", ...)` en `main()`.
2. Pasarlo a `sync_one`/`sync_all` y a su `_progress` callback si aplica.
3. Documentar en `04-manual-uso.md` y `--help`.

---

## Testing manual

### Smoke contra una sola fuente
```bash
python -m sync_catalogos.sync --catalog divipola_departamentos --dry-run
```

### Smoke contra una DB local
```bash
docker run -d --name pg -p 55432:5432 -e POSTGRES_PASSWORD=test postgres:16
python -m sync_catalogos.sync --catalog divipola_municipios \
    --db "postgresql+psycopg://postgres:test@localhost:55432/postgres" \
    --no-write-json
docker exec pg psql -U postgres -c "\d salud_divipola_municipios"
docker rm -f pg
```

Más detalle en [Pruebas §7](07-pruebas.md).

---

## Performance

### Medido en ambiente real (M1 Mac, 16 GB RAM)

| Operación                                                  | Tiempo        | Throughput            |
|------------------------------------------------------------|---------------|-----------------------|
| Sync de 1 catálogo Socrata pequeño (33 filas)              | ~1.0 s        | —                     |
| Sync de divipola_municipios (1122 filas)                   | ~1.0 s        | 1122 filas/s          |
| Sync de cie10 (14k filas, SISPRO con paginación)           | ~10 s         | 1.4k filas/s          |
| Sync de reps_servicios (228k filas, REPS export 155 MB)    | ~95 s         | 2.4k filas/s          |
| Sync masivo SISPRO (297 catálogos, 1.9M filas)             | ~25 min       | 1.3k filas/s          |
| Bulk a Postgres (273 catálogos, 6999 filas)                | ~4 s          | 1.7k filas/s          |
| Bulk a MongoDB (273 catálogos, 6999 filas)                 | ~4 s          | similar               |

### Bottlenecks observados

1. **Network → SISPRO**: cada postback (página) tarda ~1 s. Para CIE10 con 7 páginas = 7 s.
2. **Parsing → REPS export grande**: `csv.DictReader` sobre 155 MB tarda ~5 s.
3. **DB insert → Mongo bulk_write**: `ordered=False` ya está activado; con replica set podría usarse transacción.
4. **JSON write → catálogos grandes**: `json.dumps(indent=2)` sobre 855 MB de `reps_servicios` tarda ~10 s.

### Optimizaciones futuras

- Streaming CSV parser (`csv.reader` chunked) para REPS gigantes en lugar de `_parse_csv` que carga todo.
- Async / paralelo para syncs de catálogos pequeños (319 syncs serial = oportunidad).
- Compresión gzip on-disk (`*.json.gz`) para REPS servicios.
- Particionar tablas SQL grandes por departamento.

---

## Próxima lectura

- [Despliegue](06-despliegue.md) — operación productiva
- [Pruebas](07-pruebas.md) — estrategia de testing

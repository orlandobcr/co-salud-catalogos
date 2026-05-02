# 2. Arquitectura

## Vista de componentes

```
                                                    ┌──────────────────────┐
                                                    │  CLI / cron          │
                                                    │  python -m sync...   │
                                                    └──────────┬───────────┘
                                                               │
                                                               ▼
                                                    ┌──────────────────────┐
                                                    │  sync.py             │
                                                    │  - load .env         │
                                                    │  - parse args        │
                                                    │  - dispatch by kind  │
                                                    └──────┬───┬───┬───────┘
                                                           │   │   │
                ┌──────────────────────────────────────────┘   │   └─────────┐
                ▼                                              ▼             ▼
    ┌────────────────────┐                ┌──────────────────────┐ ┌──────────────────┐
    │  socrata.py        │                │  sispro.py           │ │  reps.py         │
    │  GET /resource/    │                │  POST ASPX (VIEWSTATE│ │  login + ibText  │
    │  $limit/$offset    │                │  pageSize=2000)      │ │  CSV ISO-8859-15 │
    └─────────┬──────────┘                └──────────┬───────────┘ └────────┬─────────┘
              │                                      │                      │
              └──────────────┬───────────────────────┴──────────────────────┘
                             │
                             ▼
                  ┌────────────────────┐
                  │  proxy.py          │  ← opcional, off por defecto
                  │  - ProxyPool       │     fallback automático a directo
                  │  - HttpClient      │     sticky por host
                  │  - 3 providers     │     (PROXY_LIST | PROXY_LIST_URL | 2captcha)
                  └─────────┬──────────┘
                            │
                            ▼ httpx + lxml
                ┌──────────────────────┐
                │  Internet (gov.co)   │
                └──────────────────────┘

                            ▼ raw entries: list[dict]
                  ┌────────────────────┐
                  │  db_schema.py      │
                  │  - infer types     │
                  │  - sanitize names  │
                  │  - coerce values   │
                  └─────────┬──────────┘
                            │
              ┌─────────────┼──────────────┐
              ▼             ▼              ▼
    ┌─────────────┐  ┌────────────┐  ┌─────────────┐
    │  io.py      │  │ db.py SQL  │  │ db.py Mongo │
    │  JSON file  │  │ SqlSink    │  │ MongoSink   │
    │  + sha256   │  │ SQLAlchemy │  │ pymongo     │
    └─────────────┘  └────────────┘  └─────────────┘
```

## Capas y responsabilidades

| Capa                | Módulos                          | Responsabilidad                                                  |
|---------------------|----------------------------------|------------------------------------------------------------------|
| **CLI**             | `sync.py`, `proxy_check.py`      | parse args, orquesta, formatea salida                            |
| **Sources**         | `socrata.py`, `sispro.py`, `reps.py` | scraping específico de cada portal                          |
| **Network**         | `proxy.py`                       | pool, sticky, retry/fallback, providers pluggables               |
| **Schema**          | `db_schema.py`                   | inferencia tipos, sanitize identificadores, coerce values        |
| **Sinks**           | `io.py`, `db.py`                 | persiste a disco / SQL / Mongo                                   |
| **Modelo**          | `schema.py`                      | dataclasses `CatalogFile`, `CatalogMetadata`                     |
| **Registry**        | `sources.py`                     | catálogo de catálogos: 319 entradas declaradas                   |

Cada capa **no conoce las de arriba** — los scrapers no saben de DB, los sinks no saben de la red, etc. Permite agregar fácilmente:
- Un nuevo `source` (ej. `siho.py`) sin tocar nada más.
- Un nuevo `sink` (ej. `clickhouse.py`) sin tocar scrapers.
- Un nuevo proxy `provider` sin tocar el cliente HTTP.

## Modelo de datos

### En disco (JSON)

```
catalogos_co/co/
├── institutional/
│   ├── reps_sedes.json
│   ├── reps_servicios.json          (855 MB — el más grande)
│   ├── reps_capacidades.json
│   ├── reps_habilitados.json
│   ├── reps_medidas_seguridad.json
│   ├── reps_sanciones.json
│   ├── reps_prestadores.json        (Socrata)
│   ├── eapb_codigos.json            (SISPRO)
│   ├── ips_por_nivel.json
│   ├── ips_listado_nivel.json
│   └── servicios_habilitados.json
├── clinical/                         (CIE10, CUPS, IUM, vacunas, enfermedades, ...)
├── geo/                              (DIVIPOLA, postales, vías, países)
├── rips/                             (validación / decodificación RIPS)
├── financial/                        (recobros, PILA, ARL, CCF, glosas)
├── admin/                            (tipos ID, sexo, régimen, demografía)
└── misc/                             (resto SISPRO sin categoría específica)
```

Cada archivo:
```json
{
  "metadata": {
    "name": "...", "source": "...", "source_url": "...",
    "version": "...", "license": "...", "row_count": 12345,
    "last_synced": "2026-05-02T20:22:00Z", "sha256": "ef9e..."
  },
  "entries": [ {...}, {...} ]
}
```

### En base de datos (SQL o Mongo)

Una **tabla / colección por catálogo**, con columnas tipadas inferidas:

```sql
salud_catalog_metadata               -- 1 fila por catálogo
    name, source, source_url, version, sha256, last_synced,
    row_count, table_name, schema_json, ...

salud_<catalog_name>                 -- 1 tabla por catálogo
    _idx INTEGER PRIMARY KEY
    <col_1> <inferred_type>
    <col_2> <inferred_type>
    ...
```

Ejemplo concreto:
```sql
salud_divipola_municipios (
    _idx INTEGER PK,
    cod_dpto VARCHAR(50),
    dpto VARCHAR(100),
    cod_mpio VARCHAR(50),
    nom_mpio VARCHAR(50),
    tipo_municipio VARCHAR(50),
    longitud DOUBLE PRECISION,
    latitud DOUBLE PRECISION
)

salud_sispro_etnia (
    _idx INTEGER PK,
    codigo BIGINT,                    -- 1, 2, 3, ...
    nombre VARCHAR(100),              -- "Indigena", "ROM (Gitano)", ...
    habilitado BOOLEAN,               -- inferido de SI/NO
    ...
)
```

Más detalle en [Funcionamiento §3](03-funcionamiento.md#inferencia-de-tipos) y [Deep technical §5](05-deep-technical.md#inferencia-de-schema).

## Flujo de una sincronización

```
1. CLI parsea: python -m sync_catalogos.sync --catalog reps_sedes
                                              │
2. load_env() lee .env (gitignored)           │
                                              │
3. find("reps_sedes") en REGISTRY             │
                                              │
4. should_use_proxy_for_kind("reps_export")   ─→ False (default)
                                              │
5. reps.fetch_export("sedes_reps.aspx",
                     use_proxy=False)
       │
       ├─ make_http_client(REPS_HOST, use_proxy=False)
       │     │
       │     └─→ HttpClient sin pool → directo
       │
       ├─ login()           POST /work.aspx con invitado/invitado
       ├─ GET form          captura __VIEWSTATE
       ├─ POST search       devuelve nuevo state + grid HTML
       ├─ POST ibText       devuelve CSV completo (ISO-8859-15)
       └─ _parse_csv()      retorna list[dict]
                                              │
6. _build_metadata(...)     calcula sha256, row_count, last_synced
                                              │
7. write_catalog(out_path, catalog)           ─→ catalogos_co/co/.../*.json (atomic write)
                                              │
8. (opcional) db_sink.write_catalog(catalog)
       │
       ├─ infer_schema(entries)                ─→ list[ColumnSpec]
       ├─ Table salud_reps_sedes (o coleción)  ─→ DDL si no existe
       ├─ DELETE existing rows (transacción)
       └─ INSERT bulk (chunked)
                                              │
9. CLI imprime resumen / JSON output
```

## Decisiones clave

### ¿Por qué `httpx` en lugar de `requests` o `aiohttp`?

- Soporte nativo de proxies HTTP/HTTPS/SOCKS5 (con `httpx[socks]`).
- Cliente sync limpio (cron amigable).
- TLS moderno y manejo de redirects sano.
- Cookies persistentes entre requests (esencial para REPS / SISPRO).

### ¿Por qué `lxml` y no `beautifulsoup4`?

- 5-10× más rápido en parseo de HTML grande (SISPRO devuelve grids con miles de filas).
- xpath nativo, más expresivo para extraer `__VIEWSTATE`, `<table id=...>`.
- Sin dependencias adicionales.

### ¿Por qué SQLAlchemy 2.x para SQL y `pymongo` directo para Mongo?

- SQLAlchemy unifica los 4 dialectos SQL (Postgres, MySQL, MSSQL, SQLite) con un solo código.
- Mongo es lo suficientemente distinto para tener su propio sink — no vale la pena abstraer con un ODM.
- Drivers son extras opcionales: el usuario instala solo el que necesita.

### ¿Por qué tablas tipadas y no una genérica con `data JSON`?

| Genérica `(name, idx, data JSON)` | Tipada por catálogo                            |
|-----------------------------------|------------------------------------------------|
| 1 schema fijo, simple             | 319 schemas inferidos, refleja realidad        |
| Query: extraer JSON path          | Query: SELECT directo, JOIN nativo, índices    |
| ❌ no aprovecha optimizador        | ✅ planner usa estadísticas, índices reales     |
| ❌ valores siempre TEXT            | ✅ BIGINT, DATE, BOOLEAN tipados                |
| ❌ DB no detecta cambios estruct.  | ✅ schema cambia → DDL alter (futuro)           |
| Tamaño en disco mayor             | Compresión natural por columna                 |

Tradeoff: una tabla nueva por catálogo = 319 tablas. Postgres / MySQL / MSSQL lo manejan sin problema.

### ¿Por qué proxy opcional con fallback?

Tres niveles de uso:

1. **Desarrollo local / CAC interno**: directo (default). Funciona perfecto contra los 3 sitios.
2. **Sync masivo SISPRO en producción**: proxy útil para distribuir carga (300+ tablas, 1.9M filas).
3. **Si proxy falla / no hay**: fallback automático a directo. **El sync nunca se bloquea por proxy.**

### ¿Por qué multi-root en el loader (Anonimiz integration)?

El proyecto Anonimiz consume estos catálogos como gazetteers para NER en historias clínicas. Su loader busca catálogos en orden de prioridad:

1. `Anonimiz/catalogs/` (manuales propios: `apellidos_co`, `stop_list_clinical`)
2. `co-salud-catalogos/catalogos_co/` (sincronizados)

Anonimiz puede overridear cualquier catálogo localmente sin tocar este repo. Si en el futuro otro proyecto consume desde aquí, agrega su path al inicio de la lista.

## Restricciones que respeta

| Fuente             | robots.txt        | Manejo                                                    |
|--------------------|-------------------|-----------------------------------------------------------|
| Datos Abiertos     | abierto           | rate limit con app token opcional                         |
| REPS Habilitación  | sin política      | login `invitado/invitado` (público por diseño)            |
| SISPRO             | `Disallow: /`     | requiere `--i-have-permission` obligatorio + log auditoría |

Ver [Permisos](permisos.md) para detalles legales.

## Próxima lectura

- [Funcionamiento](03-funcionamiento.md) — cómo opera cada flujo en detalle
- [Deep technical](05-deep-technical.md) — internals para quien va a contribuir

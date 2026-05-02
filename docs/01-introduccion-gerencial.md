# 1. Introducción gerencial

## Qué es

`co-salud-catalogos` es un **sincronizador reproducible de los catálogos públicos del sector salud en Colombia**. Descarga, valida y persiste — en disco como JSON o en una base de datos relacional / documental — las tablas de referencia oficiales que el ecosistema de salud usa para auditoría, validación de reportes (RIPS), análisis de cohortes, gestión de riesgos, suficiencia de prestadores y conciliación financiera.

Cubre **319 catálogos** distribuidos en tres fuentes oficiales:

| Fuente                       | Catálogos | Usos típicos                                                     |
|------------------------------|----------:|------------------------------------------------------------------|
| MinSalud REPS Habilitación   | 6         | Prestadores, sedes, servicios, capacidad instalada, sanciones    |
| MinSalud SISPRO              | ~300      | CIE-10, CUPS, IUM, EAPB, ATC, vacunas, RIPS, recobros, demografía|
| Datos Abiertos Colombia      | ~13       | DIVIPOLA, códigos postales, vías INVIAS, glosario médico, PBS    |

Datos resultantes: **2.5 M filas, ~3 GB en disco**.

## Para qué sirve

| Objetivo de negocio                              | Cómo lo resuelve                                                    |
|--------------------------------------------------|---------------------------------------------------------------------|
| **Auditoría de RIPS**                            | Tablas de referencia listas para `JOIN` con datos transaccionales: tipos de servicio, vía de ingreso, estado de salida, finalidad por sexo/edad |
| **Análisis de cohortes alto costo**              | Catálogo `enfermedad_huerfana`, `tipo_diagnostico_principal`, ENT/transmisibles, tamizajes de cáncer |
| **Validación de prestadores**                    | REPS Sedes (76k), Servicios (228k), Capacidad (97k), Sanciones, Medidas de seguridad |
| **Conciliación financiera**                      | Recobros, PILA, glosas, causas de negación, EAPB por NIT, planes de beneficio |
| **Geocodificación / cobertura**                  | DIVIPOLA dpto/mpio/centro poblado, códigos postales, vías          |
| **Análisis de medicamentos / suficiencia**       | IUM, CUM INVIMA, ATC WHO, registros sanitarios, dispositivos       |

En lugar de que cada equipo gaste semanas en **cazar PDFs sueltos, copiar tablas a Excel, parsear ASPX a mano y mantenerlas vigentes**, este repo lo hace en **una corrida automática** con metadata reproducible (URL fuente, versión, sha256, fecha de sync) lista para auditarse.

## Quién debería usarlo

- **Equipos de auditoría en salud** (públicos y privados)
- **Cuentas de alto costo / observatorios epidemiológicos**
- **Áreas de validación de RIPS** en EPS / IPS
- **Equipos de gestión de riesgo** (ARL, EAPB)
- **Analistas de datos** que cruzan información del sector con cohortes propias
- **Investigadores** que necesitan tablas oficiales con trazabilidad

## Valor entregado

| Métrica                              | Antes                                            | Con este proyecto                            |
|--------------------------------------|--------------------------------------------------|----------------------------------------------|
| Tiempo para tener todos los catálogos al día | semanas (manual, fragmentado)            | **~25 min** (1 comando)                      |
| Trazabilidad de cada dato            | "lo descargamos hace meses, no recordamos"       | metadata con URL, versión, sha256, timestamp |
| Cobertura                            | parcial — los más conocidos                      | **319 catálogos**, 6 fuentes REPS completas  |
| Consumo desde apps                   | leer Excels manualmente                          | JOIN SQL nativo o agregaciones MongoDB       |
| Costos recurrentes                   | tiempo del equipo                                | infraestructura mínima (sync scheduling)     |

## Casos de uso ya validados

1. **Pipeline de anonimización clínica** — usa REPS sedes/prestadores, EAPB, DIVIPOLA y stop-lists clínicas (CIE/CUPS/IUM) como gazetteers para detectar entidades en historias clínicas.
2. **Auditoría retroactiva** — JOIN de RIPS reportados vs catálogos vigentes en la fecha del servicio (versión y sha256 de cada catálogo permite reconstruir el snapshot histórico).
3. **Análisis de oportunidad de atención** — cruce de servicios habilitados (REPS) con sedes geocoded (DIVIPOLA + códigos postales).

## Lo que NO es

- **No es un repositorio de datos confidenciales** — solo contiene catálogos *públicos*. Cero PII de pacientes.
- **No reemplaza a SISPRO ni REPS** — los expone en un formato consumible. La fuente de verdad sigue siendo MinSalud.
- **No es un servicio en línea** — es una librería + CLI. No expone HTTP API por sí mismo.
- **No bypassa restricciones legales** — respeta robots.txt; SISPRO requiere consentimiento operativo explícito documentado por el operador.

## Costos y dependencias

- **Software**: 100 % open source (MIT). Dependencias: `httpx`, `lxml`, opcionalmente `sqlalchemy`, `psycopg`, `pymysql`, `pyodbc`, `pymongo`.
- **Infraestructura**: ~3 GB de almacenamiento si se mantiene en disco; menos en DB con compresión natural; 1 vCPU + 2 GB RAM bastan para correr el sync.
- **Tiempo recurrente**: cron semanal de Socrata + REPS = ~5 min total. SISPRO trimestral con consentimiento manual = ~25 min.
- **Sin licencias propietarias**.

## Riesgos y mitigaciones

| Riesgo                                                     | Mitigación implementada                                              |
|------------------------------------------------------------|----------------------------------------------------------------------|
| MinSalud cambia el formato de un endpoint                  | Cada scraper (`socrata`, `sispro`, `reps`) está aislado; un fallo no bloquea los demás |
| robots.txt restrictivo de SISPRO                           | Flag `--i-have-permission` obligatorio; documentado en `permisos.md` |
| Bloqueo de IP por exceso de tráfico                        | Pool de proxies opcional con fallback automático a directo; rate limit tokens en Socrata |
| Cambio en estructura de un catálogo (nueva columna)        | Schema inferido automáticamente en cada sync; metadata.sha256 detecta cambios |
| Pérdida del JSON local                                     | Regenerable con un comando; nada del repo es no-recuperable          |

## Hoja de ruta

| Estado     | Iniciativa                                                                |
|------------|---------------------------------------------------------------------------|
| ✅ Done    | Sync de las 3 fuentes (Socrata, SISPRO, REPS) con 319 catálogos          |
| ✅ Done    | Persistencia en disco (JSON), Postgres, MySQL, MSSQL, MongoDB, SQLite     |
| ✅ Done    | Pool de proxies pluggable con fallback automático                         |
| ✅ Done    | Schema tipado por catálogo con inferencia desde datos reales              |
| ⏳ Backlog | Deduplicación de paginación SISPRO (CIE-10/CUPS/IUM)                      |
| ⏳ Backlog | Particionamiento de catálogos masivos (REPS servicios = 855 MB)           |
| ⏳ Backlog | Webhook de notificación cuando un catálogo cambia (sha256 distinto)        |

## Próximas lecturas

- [Arquitectura](02-arquitectura.md) — diagrama de componentes y decisiones de diseño
- [Funcionamiento](03-funcionamiento.md) — flujos paso a paso
- [Manual de uso](04-manual-uso.md) — comandos y ejemplos
- [Deep technical](05-deep-technical.md) — para quien va a tocar código
- [Despliegue](06-despliegue.md) — operación en producción
- [Pruebas](07-pruebas.md) — estrategia de testing
- [Inventario de fuentes](inventario_fuentes.md) — esquema de cada catálogo
- [Permisos](permisos.md) — régimen legal por fuente
- [Proxy](proxy.md) — pool de proxies

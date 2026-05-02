# Permisos y consideraciones legales

Este documento registra el régimen de acceso para cada fuente externa que el sincronizador toca.

---

## 1. Datos Abiertos Colombia (Socrata)

- **Host**: `www.datos.gov.co`
- **API**: SODA REST pública.
- **robots.txt**: abierto (no restringe `/resource/`).
- **Marco legal**: Ley 1712 de 2014 — Ley de Transparencia y Acceso a la Información.
- **Permiso**: ninguno requerido. Solo se recomienda usar `X-App-Token` para subir el rate limit (ver `SALUD_SOCRATA_APP_TOKEN`).
- **Rate limit**: ~1k requests/h sin token, ~100k/h con token.

Sin restricciones operativas. Apto para cron periódico.

---

## 2. MinSalud SISPRO (web.sispro.gov.co)

- **Host**: `web.sispro.gov.co`
- **Endpoint**: `/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=<X>`
- **robots.txt**: `Disallow: /` ⚠️ — bloquea explícitamente todo crawling automático.
- **Marco legal**: las tablas (CIE-10, CUPS, IUM, EAPB, etc.) son de uso público bajo MinSalud.
- **Permiso**: el bloqueo en `robots.txt` aplica a crawlers genéricos. **El operador del repo es responsable de obtener y documentar su propio permiso operativo del MinSalud antes de activar este kind.** El consentimiento técnico (flag `--i-have-permission`) declara que el operador asume esa responsabilidad.

### Reglas operativas recomendadas

1. **Cada ejecución debe ser manual y documentada** en bitácora interna (operador, fecha, propósito, justificación).
2. El flag `--i-have-permission` en el CLI es obligatorio para activar este kind:
   ```bash
   python -m sync_catalogos.sync --catalog cie10 --i-have-permission
   python -m sync_catalogos.sync --all --kind sispro_aspx --i-have-permission
   ```
3. **NO se debe poner en cron automático.** El permiso operativo es siempre puntual, no general.
4. Si MinSalud actualiza su `robots.txt` o solicita pausar, suspender inmediatamente.
5. Cadencia razonable: una vez por trimestre para CIE-10/CUPS, una por mes para IUM. Más frecuente solo bajo justificación operativa explícita.

Catálogos cubiertos por este kind: CIE-10, CUPS, IUM, EAPB y ~290 tablas adicionales de referencia.

---

## 3. MinSalud REPS Habilitación (prestadores.minsalud.gov.co)

- **Host**: `prestadores.minsalud.gov.co`
- **Endpoint**: `/habilitacion/consultas/<página>_reps.aspx`
- **robots.txt**: 404 — no existe política restrictiva.
- **Acceso**: portal web público con login `invitado / invitado` (credenciales por diseño para consulta pública).
- **Mecanismo de export**: el sincronizador usa el botón oficial "Exportar a Texto" (`ibText`) que MinSalud expone en cada formulario de consulta.

### Consideraciones

1. El portal está concebido para consulta pública: el mismo botón "Exportar" permite a cualquier ciudadano descargar los mismos archivos.
2. El sincronizador **no** elude protecciones técnicas — usa el flujo normal del formulario.
3. La cadencia recomendada es semanal. Apto para cron.
4. Mantener `User-Agent` identificable (default: `co-salud-catalogos/0.x`).

Catálogos cubiertos: `reps_habilitados`, `reps_sedes`, `reps_servicios`, `reps_capacidades`, `reps_medidas_seguridad`, `reps_sanciones`.

---

## 4. Buenas prácticas generales

- **Atomic write**: cada catálogo se escribe en `tempfile.tmp` y luego se renombra (no deja archivos parciales si hay corte).
- **Hash sha256** del contenido en `metadata.sha256` — permite detectar cambios silenciosos.
- **Versión**: `metadata.version` apunta al `rowsUpdatedAt` de Socrata o a la fecha de sync para SISPRO/REPS.
- **No se almacenan credenciales** — el login REPS usa `invitado/invitado` hardcoded (es público); SISPRO no requiere credencial.

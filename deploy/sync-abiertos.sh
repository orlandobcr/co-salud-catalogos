#!/bin/bash
# Sincronización semanal de las fuentes abiertas (Datos Abiertos + REPS) y corte
# del estado resultante. SISPRO no va aquí: exige --i-have-permission y corrida
# manual documentada (docs/permisos.md).
#
# Corre como `cosalud` desde co-salud-sync-abiertos.service, con el .env cargado.
set -uo pipefail
cd /opt/co-salud-catalogos
PY=.venv/bin/python
CORTES_ROOT="${SALUD_CORTES_ROOT:-/var/lib/co-salud/cortes}"

rc=0
$PY -m sync_catalogos.sync --all --kind socrata --db "$SALUD_API_DB_URL" --no-write-json || rc=1
$PY -m sync_catalogos.sync --all --kind reps_export --db "$SALUD_API_DB_URL" --no-write-json || rc=1
# El corte se toma aunque algún catálogo haya fallado: refleja lo que el API
# está sirviendo, que es lo que importa conservar.
$PY -m sync_catalogos.cortes --root "$CORTES_ROOT" crear --db "$SALUD_API_DB_URL" || rc=1
exit $rc

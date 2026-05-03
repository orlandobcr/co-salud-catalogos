"""Endpoints de exploración cross-catálogo.

Esta capa NO consulta una sola tabla — agrega información de varias para
construir vistas con sentido de negocio:

  /explore/geo/...          → DIVIPOLA + conteos en REPS
  /explore/prestadores      → búsqueda con filtros en cascada
  /explore/prestador/{id}   → vista 360 con todas sus "paticas"
  /explore/cie10/{codigo}   → detalle de un diagnóstico
  /explore/cups/{codigo}    → detalle de un procedimiento
  /explore/medicamento/{id} → detalle IUM

Modelo freemium:
- Las LISTAS y BÚSQUEDAS resumen son siempre visibles (estructura abierta).
- Las VISTAS 360 marcan secciones como `premium_locked: true` cuando el usuario
  no tiene permiso al catálogo subyacente. El frontend muestra esas secciones
  con un teaser + CTA "habla con comercial".
"""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy import text

from ..auth import CurrentUser, get_current_user
from ..db import query_raw
from ..semantic_columns import (
    GEO_PUBLIC_CATALOGS,
    divipola_to_reps_dpto_names,
    reps_to_divipola_dpto_name,
)


def _build_in_clause_dpto(nombre_dpto: str | None, params: dict, prefix: str = "dpto") -> str | None:
    """Construye `upper(depa_nombre) IN (...)` expandiendo los Distritos Especiales.
    Modifica `params` en-place. Devuelve la cláusula SQL o None si no hay filtro."""
    if not nombre_dpto:
        return None
    reps_names = divipola_to_reps_dpto_names(nombre_dpto)
    placeholders = []
    for i, name in enumerate(reps_names):
        key = f"{prefix}_{i}"
        params[key] = name.upper()
        placeholders.append(f":{key}")
    return f"upper(depa_nombre) IN ({', '.join(placeholders)})"


router = APIRouter(prefix="/api/v1/explore", tags=["explore (cross-catálogo)"])


# ---------------------------------------------------------------------------
# Permisos freemium
# ---------------------------------------------------------------------------

PREMIUM_REPS_CATALOGS = {
    "reps_prestadores", "reps_habilitados", "reps_sedes",
    "reps_servicios", "reps_capacidades",
    "reps_sanciones", "reps_medidas_seguridad",
}

PREMIUM_CLINICAL = {
    "cie10", "cups", "ium_medicamentos",
    "procedimientos_pbs", "medicamentos_pbs",
}


def _user_has(user: CurrentUser, catalog: str) -> bool:
    return user.is_super_admin or catalog in GEO_PUBLIC_CATALOGS or catalog in user.permissions


# ---------------------------------------------------------------------------
# GEO — siempre abierto (DIVIPOLA es info pública trivial)
# ---------------------------------------------------------------------------

@router.get(
    "/geo/departamentos",
    summary="Lista de los 33 departamentos con conteos opcionales",
)
def geo_departamentos(
    request: Request,
    with_counts: bool = Query(True, description="Incluye conteo de prestadores REPS por dpto"),
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine
    base = query_raw(engine, """
        SELECT codigo_departamento, nombre_departamento, latitud, longitud
        FROM salud_divipola_departamentos
        ORDER BY nombre_departamento
    """)
    if not with_counts:
        return {"items": base}

    counts: dict[str, int] = {}
    try:
        for r in query_raw(engine, """
            SELECT depa_nombre AS d, COUNT(DISTINCT codigo_habilitacion) AS n
            FROM salud_reps_habilitados
            WHERE depa_nombre IS NOT NULL
            GROUP BY depa_nombre
        """):
            divipola_name = reps_to_divipola_dpto_name(r["d"])
            if divipola_name:
                counts[divipola_name] = counts.get(divipola_name, 0) + (r["n"] or 0)
    except Exception:
        counts = {}

    for it in base:
        key = (it.get("nombre_departamento") or "").strip()
        it["prestadores_count"] = counts.get(key, 0)
    return {"items": base}


@router.get(
    "/geo/municipios",
    summary="Municipios filtrados por departamento (con conteos)",
)
def geo_municipios(
    request: Request,
    cod_dpto: str | None = Query(None, description="Código DIVIPOLA del depto (2 dígitos)"),
    nombre_dpto: str | None = Query(None, description="Nombre del depto (alternativa al código)"),
    with_counts: bool = Query(True),
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine
    where_parts = []
    params: dict[str, Any] = {}
    if cod_dpto:
        where_parts.append("cod_dpto = :cod_dpto")
        params["cod_dpto"] = cod_dpto
    elif nombre_dpto:
        where_parts.append("upper(dpto) = upper(:nombre_dpto)")
        params["nombre_dpto"] = nombre_dpto
    where = (" WHERE " + " AND ".join(where_parts)) if where_parts else ""

    municipios = query_raw(engine, f"""
        SELECT cod_dpto, dpto, cod_mpio, nom_mpio, tipo_municipio, latitud, longitud
        FROM salud_divipola_municipios
        {where}
        ORDER BY nom_mpio
    """, params)

    if not with_counts:
        return {"items": municipios, "total": len(municipios)}

    counts: dict[str, int] = {}
    try:
        sub_where = ""
        sub_params: dict[str, Any] = {}
        depto_name = nombre_dpto or (municipios[0]["dpto"] if municipios else None)
        if depto_name:
            in_clause = _build_in_clause_dpto(depto_name, sub_params, "dpto")
            if in_clause:
                sub_where = " WHERE " + in_clause
        for r in query_raw(engine, f"""
            SELECT muni_nombre AS m, COUNT(DISTINCT codigo_habilitacion) AS n
            FROM salud_reps_habilitados
            {sub_where}
            GROUP BY muni_nombre
        """, sub_params):
            if r["m"]:
                counts[r["m"].strip().upper()] = r["n"]
    except Exception:
        counts = {}

    for it in municipios:
        key = (it.get("nom_mpio") or "").strip().upper()
        it["prestadores_count"] = counts.get(key, 0)

    return {"items": municipios, "total": len(municipios)}


# ---------------------------------------------------------------------------
# PRESTADORES — buscador con filtros en cascada
# ---------------------------------------------------------------------------

@router.get(
    "/prestadores",
    summary="Buscador de prestadores REPS con filtros geográficos/clínicos",
    description=(
        "Acepta filtros: nombre_dpto, nombre_mpio, clase_prestador, "
        "naturaleza_juridica, ese (true/false), serv_codigo (servicio habilitado), "
        "grse_codigo (grupo de servicio), q (búsqueda por nombre/NIT). "
        "Devuelve lista resumen — el detalle 360 va en /prestador/{codigo_habilitacion}."
    ),
)
def search_prestadores(
    request: Request,
    nombre_dpto: str | None = None,
    nombre_mpio: str | None = None,
    clase_prestador: str | None = Query(None, description="clpr_nombre (ej. IPS, Profesional Independiente)"),
    naturaleza: str | None = Query(None, description="naju_nombre"),
    ese: bool | None = None,
    serv_codigo: str | None = Query(None, description="Código de servicio REPS (filtra a prestadores que ofrecen ese servicio)"),
    grse_codigo: str | None = Query(None, description="Código de grupo de servicio"),
    q: str | None = Query(None, description="Búsqueda en nombre_prestador o NIT"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine

    where = ["1=1"]
    params: dict[str, Any] = {}

    use_servicios = bool(serv_codigo or grse_codigo)
    table = "salud_reps_servicios" if use_servicios else "salud_reps_habilitados"

    if nombre_dpto:
        in_clause = _build_in_clause_dpto(nombre_dpto, params, "dpto")
        if in_clause:
            where.append(in_clause)
    if nombre_mpio:
        where.append("upper(muni_nombre) = upper(:nombre_mpio)")
        params["nombre_mpio"] = nombre_mpio
    if clase_prestador:
        where.append("upper(clpr_nombre) like upper(:clase)")
        params["clase"] = f"%{clase_prestador}%"
    if naturaleza:
        where.append("upper(naju_nombre) like upper(:naju)")
        params["naju"] = f"%{naturaleza}%"
    if ese is not None:
        if use_servicios:
            where.append("upper(ese) = :ese")
            params["ese"] = "TRUE" if ese else "FALSE"
        else:
            where.append("ese = :ese")
            params["ese"] = ese
    if use_servicios and serv_codigo:
        where.append("serv_codigo = :serv_codigo")
        params["serv_codigo"] = serv_codigo
    if use_servicios and grse_codigo:
        where.append("grse_codigo = :grse_codigo")
        params["grse_codigo"] = grse_codigo
    if q:
        where.append("(upper(nombre_prestador) like upper(:q) OR cast(nits_nit as text) like :qraw)")
        params["q"] = f"%{q}%"
        params["qraw"] = f"%{q}%"

    where_sql = " AND ".join(where)

    count_row = query_raw(engine, f"""
        SELECT count(DISTINCT codigo_habilitacion) AS n
        FROM {table}
        WHERE {where_sql}
    """, params)
    total = count_row[0]["n"] if count_row else 0

    rows = query_raw(engine, f"""
        SELECT DISTINCT
            codigo_habilitacion,
            nombre_prestador,
            depa_nombre AS departamento,
            muni_nombre AS municipio,
            clpr_nombre AS clase_prestador,
            nits_nit AS nit,
            ese
        FROM {table}
        WHERE {where_sql}
        ORDER BY nombre_prestador
        LIMIT :limit OFFSET :offset
    """, {**params, "limit": limit, "offset": offset})

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "filters_applied": {
            k: v for k, v in {
                "nombre_dpto": nombre_dpto, "nombre_mpio": nombre_mpio,
                "clase_prestador": clase_prestador, "naturaleza": naturaleza,
                "ese": ese, "serv_codigo": serv_codigo, "grse_codigo": grse_codigo, "q": q,
            }.items() if v is not None
        },
        "items": rows,
    }


@router.get(
    "/prestadores/filters",
    summary="Devuelve listas de valores para popular dropdowns de filtros",
)
def prestador_filter_options(
    request: Request,
    nombre_dpto: str | None = None,
    nombre_mpio: str | None = None,
    user: CurrentUser = Depends(get_current_user),
):
    """Retorna distinct values para clases, naturalezas, grupos de servicio.
    Usado para alimentar dropdowns que se cargan según el contexto geográfico ya elegido."""
    engine = request.app.state.engine
    where = ["1=1"]
    params: dict[str, Any] = {}
    if nombre_dpto:
        in_clause = _build_in_clause_dpto(nombre_dpto, params, "dpto")
        if in_clause:
            where.append(in_clause)
    if nombre_mpio:
        where.append("upper(muni_nombre) = upper(:mpio)")
        params["mpio"] = nombre_mpio
    where_sql = " AND ".join(where)

    clases = [r["v"] for r in query_raw(engine, f"""
        SELECT DISTINCT clpr_nombre AS v FROM salud_reps_habilitados
        WHERE {where_sql} AND clpr_nombre IS NOT NULL
        ORDER BY v
    """, params)]
    naturalezas = [r["v"] for r in query_raw(engine, f"""
        SELECT DISTINCT naju_nombre AS v FROM salud_reps_habilitados
        WHERE {where_sql} AND naju_nombre IS NOT NULL
        ORDER BY v
    """, params)]

    grupos_servicio = []
    try:
        grupos_servicio = query_raw(engine, f"""
            SELECT DISTINCT grse_codigo, grse_nombre
            FROM salud_reps_servicios
            WHERE {where_sql} AND grse_nombre IS NOT NULL
            ORDER BY grse_nombre
            LIMIT 100
        """, params)
    except Exception:
        pass

    return {
        "clases_prestador": clases,
        "naturalezas_juridicas": naturalezas,
        "grupos_servicio": grupos_servicio,
    }


@router.get(
    "/prestadores/servicios",
    summary="Lista de servicios disponibles (para autocomplete del filtro `servicio`)",
)
def prestador_servicios_options(
    request: Request,
    grse_codigo: str | None = None,
    q: str | None = None,
    nombre_dpto: str | None = None,
    nombre_mpio: str | None = None,
    limit: int = Query(200, ge=1, le=2000),
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine
    where = ["serv_codigo IS NOT NULL"]
    params: dict[str, Any] = {"limit": limit}
    if grse_codigo:
        where.append("grse_codigo = :grse_codigo")
        params["grse_codigo"] = grse_codigo
    if nombre_dpto:
        in_clause = _build_in_clause_dpto(nombre_dpto, params, "dpto")
        if in_clause:
            where.append(in_clause)
    if nombre_mpio:
        where.append("upper(muni_nombre) = upper(:mpio)")
        params["mpio"] = nombre_mpio
    if q:
        where.append("upper(serv_nombre) like upper(:q)")
        params["q"] = f"%{q}%"
    where_sql = " AND ".join(where)
    rows = query_raw(engine, f"""
        SELECT DISTINCT serv_codigo, serv_nombre, grse_codigo, grse_nombre
        FROM salud_reps_servicios
        WHERE {where_sql}
        ORDER BY serv_nombre
        LIMIT :limit
    """, params)
    return {"items": rows, "count": len(rows)}


# ---------------------------------------------------------------------------
# VISTA 360 PRESTADOR — todas las "paticas" agregadas
# ---------------------------------------------------------------------------

def _section(catalog: str, user: CurrentUser, fetch_fn):
    """Wrapper que retorna {data:..., premium_locked:bool}.
    Si el usuario no tiene acceso al catálogo, NO ejecuta el fetch."""
    if not _user_has(user, catalog):
        return {"premium_locked": True, "catalog_required": catalog, "data": None}
    try:
        return {"premium_locked": False, "catalog_required": catalog, "data": fetch_fn()}
    except Exception as e:
        return {"premium_locked": False, "catalog_required": catalog,
                "data": None, "error": str(e)}


@router.get(
    "/prestador/{codigo_habilitacion}",
    summary="Vista 360 de un prestador (identidad + sedes + servicios + capacidades + sanciones)",
)
def prestador_360(
    codigo_habilitacion: str,
    request: Request,
    user: CurrentUser = Depends(get_current_user),
):
    engine = request.app.state.engine

    identidad = None
    try:
        rows = query_raw(engine, """
            SELECT * FROM salud_reps_habilitados
            WHERE codigo_habilitacion = :ch
            LIMIT 1
        """, {"ch": codigo_habilitacion})
        identidad = rows[0] if rows else None
    except Exception:
        identidad = None

    if not identidad:
        try:
            rows = query_raw(engine, """
                SELECT DISTINCT codigo_habilitacion, nombre_prestador,
                       depa_nombre AS departamento, muni_nombre AS municipio
                FROM salud_reps_servicios
                WHERE codigo_habilitacion = :ch
                LIMIT 1
            """, {"ch": codigo_habilitacion})
            identidad = rows[0] if rows else None
        except Exception:
            pass

    if not identidad:
        raise HTTPException(status_code=404, detail=f"Prestador {codigo_habilitacion} no encontrado")

    sedes = _section("reps_sedes", user, lambda: query_raw(engine, """
        SELECT departamento, municipio, codigo_prestador, codigo_habilitacion, numero_sede,
               nombre, gerente, tipo_zona, direccion, barrio, telefono, email,
               fecha_apertura, fecha_cierre, sede_principal, habilitado
        FROM salud_reps_sedes
        WHERE codigo_habilitacion = :ch
        ORDER BY numero_sede
    """, {"ch": codigo_habilitacion}))

    servicios = _section("reps_servicios", user, lambda: query_raw(engine, """
        SELECT numero_sede, sede_nombre, grse_codigo, grse_nombre,
               serv_codigo, serv_nombre, nivel, complejidad_baja, complejidad_media,
               complejidad_alta, ambulatorio, hospitalario, unidad_movil, domiciliario,
               fecha_apertura, fecha_cierre, habilitado
        FROM salud_reps_servicios
        WHERE codigo_habilitacion = :ch
        ORDER BY numero_sede, grse_nombre, serv_nombre
        LIMIT 1000
    """, {"ch": codigo_habilitacion}))

    capacidades = _section("reps_capacidades", user, lambda: query_raw(engine, """
        SELECT numero_sede, sede_nombre, grupo_capacidad, coca_codigo, coca_nombre,
               cantidad, modalidad, modelo, numero_placa
        FROM salud_reps_capacidades
        WHERE codigo_habilitacion = :ch
        ORDER BY numero_sede, grupo_capacidad
    """, {"ch": codigo_habilitacion}))

    sanciones = _section("reps_sanciones", user, lambda: query_raw(engine, """
        SELECT * FROM salud_reps_sanciones
        WHERE codigo_habilitacion = :ch
        ORDER BY 1 DESC
        LIMIT 100
    """, {"ch": codigo_habilitacion}))

    medidas = _section("reps_medidas_seguridad", user, lambda: query_raw(engine, """
        SELECT * FROM salud_reps_medidas_seguridad
        WHERE codigo_habilitacion = :ch
        ORDER BY 1 DESC
        LIMIT 100
    """, {"ch": codigo_habilitacion}))

    # Geo: lat/long del municipio del prestador (DIVIPOLA, abierto)
    geo = None
    muni_nombre = identidad.get("muni_nombre") or identidad.get("municipio")
    if muni_nombre:
        try:
            geo_rows = query_raw(engine, """
                SELECT cod_dpto, dpto, cod_mpio, nom_mpio, latitud, longitud
                FROM salud_divipola_municipios
                WHERE upper(nom_mpio) = upper(:m)
                LIMIT 1
            """, {"m": muni_nombre})
            geo = geo_rows[0] if geo_rows else None
        except Exception:
            pass

    summary_view = {
        "codigo_habilitacion": identidad.get("codigo_habilitacion"),
        "nombre_prestador": identidad.get("nombre_prestador"),
        "razon_social": identidad.get("razon_social"),
        "nit": identidad.get("nits_nit"),
        "departamento": identidad.get("depa_nombre") or identidad.get("departamento"),
        "municipio": identidad.get("muni_nombre") or identidad.get("municipio"),
        "clase_prestador": identidad.get("clpr_nombre"),
        "naturaleza_juridica": identidad.get("naju_nombre"),
        "ese": identidad.get("ese"),
        "nivel": identidad.get("nivel"),
        "habilitado": identidad.get("habilitado"),
        "telefono": identidad.get("telefono"),
        "email": identidad.get("email"),
        "direccion": identidad.get("direccion"),
        "rep_legal": identidad.get("rep_legal"),
        "gerente": identidad.get("gerente"),
        "fecha_radicacion": identidad.get("fecha_radicacion"),
        "fecha_vencimiento": identidad.get("fecha_vencimiento"),
    }
    if not _user_has(user, "reps_habilitados"):
        for sensitive in ("nit", "telefono", "email", "direccion", "rep_legal",
                          "gerente", "razon_social", "fecha_radicacion", "fecha_vencimiento"):
            summary_view[sensitive] = None
        summary_view["_premium_fields_locked"] = True

    return {
        "summary": summary_view,
        "geo": geo,
        "sections": {
            "sedes": sedes,
            "servicios": servicios,
            "capacidades": capacidades,
            "sanciones": sanciones,
            "medidas_seguridad": medidas,
        },
    }


# ---------------------------------------------------------------------------
# DETALLE CLÍNICO — CIE-10, CUPS, IUM
# ---------------------------------------------------------------------------

def _clinical_detail(engine, table: str, codigo: str, name: str) -> dict:
    rows = query_raw(engine, f"""
        SELECT * FROM {table} WHERE codigo = :c LIMIT 5
    """, {"c": codigo})
    if not rows:
        raise HTTPException(status_code=404, detail=f"{name} {codigo} no encontrado")
    return {"codigo": codigo, "registros": rows}


@router.get("/cie10/{codigo}", summary="Detalle de un código CIE-10")
def cie10_detail(codigo: str, request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    if not _user_has(user, "cie10"):
        raise HTTPException(
            status_code=402,
            detail={
                "error_code": "PERMISSION_REQUIRED", "catalog": "cie10",
                "message": "El catálogo CIE-10 requiere acceso premium.",
            },
        )
    return _clinical_detail(engine, "salud_cie10", codigo, "CIE-10")


@router.get("/cups/{codigo}", summary="Detalle de un código CUPS")
def cups_detail(codigo: str, request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    if not _user_has(user, "cups"):
        raise HTTPException(
            status_code=402,
            detail={
                "error_code": "PERMISSION_REQUIRED", "catalog": "cups",
                "message": "El catálogo CUPS requiere acceso premium.",
            },
        )
    return _clinical_detail(engine, "salud_cups", codigo, "CUPS")


@router.get("/medicamento/{codigo}", summary="Detalle de un medicamento IUM")
def ium_detail(codigo: str, request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    if not _user_has(user, "ium_medicamentos"):
        raise HTTPException(
            status_code=402,
            detail={
                "error_code": "PERMISSION_REQUIRED", "catalog": "ium_medicamentos",
                "message": "El catálogo IUM (medicamentos) requiere acceso premium.",
            },
        )
    return _clinical_detail(engine, "salud_ium_medicamentos", codigo, "IUM")


# ---------------------------------------------------------------------------
# Stats globales (para overview cards en la pestaña Explorar)
# ---------------------------------------------------------------------------

@router.get("/stats", summary="Métricas agregadas del sistema (para tarjetas overview)")
def explore_stats(request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    out: dict[str, Any] = {}
    try:
        out["departamentos"] = query_raw(engine, "SELECT count(*) AS n FROM salud_divipola_departamentos")[0]["n"]
    except Exception:
        out["departamentos"] = None
    try:
        out["municipios"] = query_raw(engine, "SELECT count(*) AS n FROM salud_divipola_municipios")[0]["n"]
    except Exception:
        out["municipios"] = None
    try:
        out["prestadores_habilitados"] = query_raw(
            engine,
            "SELECT count(DISTINCT codigo_habilitacion) AS n FROM salud_reps_habilitados",
        )[0]["n"]
    except Exception:
        out["prestadores_habilitados"] = None
    try:
        out["sedes"] = query_raw(engine, "SELECT count(*) AS n FROM salud_reps_sedes")[0]["n"]
    except Exception:
        out["sedes"] = None
    try:
        out["servicios_habilitados"] = query_raw(engine, "SELECT count(*) AS n FROM salud_reps_servicios")[0]["n"]
    except Exception:
        out["servicios_habilitados"] = None
    try:
        out["cie10_codigos"] = query_raw(engine, "SELECT count(*) AS n FROM salud_cie10")[0]["n"]
    except Exception:
        out["cie10_codigos"] = None
    try:
        out["cups_codigos"] = query_raw(engine, "SELECT count(*) AS n FROM salud_cups")[0]["n"]
    except Exception:
        out["cups_codigos"] = None
    try:
        out["medicamentos_ium"] = query_raw(engine, "SELECT count(*) AS n FROM salud_ium_medicamentos")[0]["n"]
    except Exception:
        out["medicamentos_ium"] = None
    return out

"""Mapeo semántico de columnas cross-catálogo.

Distintos catálogos guardan la misma información geográfica/institucional bajo
nombres de columna distintos (ej. `codigo_departamento` en DIVIPOLA vs
`depa_nombre` en REPS servicios vs `departamentoprestadordesc` en REPS prestadores).
Este módulo concentra el mapeo y expone helpers para resolver una "clave conceptual"
contra una tabla concreta sin necesidad de hardcodear nombres en cada lugar.
"""

from __future__ import annotations

from typing import Iterable

from sqlalchemy import Table


# Concepto → lista de variantes ordenadas por preferencia (la primera que exista
# en la tabla es la que se usa).
SEMANTIC_COLUMNS: dict[str, list[str]] = {
    # Geográficas
    "departamento_codigo": ["codigo_departamento", "cod_dpto"],
    "departamento_nombre": [
        "nombre_departamento", "dpto", "depa_nombre", "departamento",
        "departamentoprestadordesc", "departamentodededesc",
    ],
    "municipio_codigo": ["codigo_municipio", "cod_mpio"],
    "municipio_nombre": [
        "nombre_municipio", "nom_mpio", "muni_nombre", "municipio",
        "municipio_prestador", "municipiosededesc", "municipiosede",
    ],
    "latitud": ["latitud", "latitude", "lat"],
    "longitud": ["longitud", "longitude", "lon", "lng"],

    # Institucionales (REPS)
    "prestador_codigo": [
        "codigo_habilitacion", "habi_codigo_habilitacion",
        "codigo_prestador", "codigoprestador",
    ],
    "prestador_nombre": ["nombre_prestador", "nombreprestador"],
    "prestador_nit": ["nits_nit", "numeroidentificacion"],
    "prestador_razon_social": ["razon_social"],

    "sede_numero": ["numero_sede"],
    "sede_nombre": ["sede_nombre", "nombresede", "nombre"],
    "sede_principal": ["numero_sede_principal"],

    # Servicios REPS
    "servicio_codigo": ["serv_codigo"],
    "servicio_nombre": ["serv_nombre"],
    "grupo_servicio_codigo": ["grse_codigo"],
    "grupo_servicio_nombre": ["grse_nombre"],

    # Capacidades
    "capacidad_codigo": ["coca_codigo"],
    "capacidad_nombre": ["coca_nombre"],
    "capacidad_grupo": ["grupo_capacidad"],
    "capacidad_cantidad": ["cantidad"],

    # Clase prestador
    "clase_prestador_codigo": ["clpr_codigo"],
    "clase_prestador_nombre": ["clpr_nombre", "claseprestador"],
    "naturaleza_juridica_nombre": ["naju_nombre", "naturalezajuridica"],
    "naturaleza_juridica_codigo": ["naju_codigo"],

    # Direcciones / contacto
    "direccion": ["direccion", "direcci_nsede", "direccionprestador"],
    "telefono": ["telefono", "telefonoprestador", "t_lefonosede"],
    "email": ["email", "email_prestador", "email_sede"],

    # Códigos clínicos (para los catálogos "tipo SISPRO")
    "codigo": ["codigo"],
    "nombre": ["nombre"],
    "descripcion": ["descripcion"],
    "habilitado": ["habilitado"],
}


def resolve(table: Table, concept: str) -> str | None:
    """Devuelve el nombre de columna concreto en `table` para el concepto dado.

    Si ninguna variante del concepto existe en la tabla, devuelve None.
    """
    variants = SEMANTIC_COLUMNS.get(concept, [])
    cols = {c.name for c in table.c}
    for v in variants:
        if v in cols:
            return v
    return None


def resolve_many(table: Table, concepts: Iterable[str]) -> dict[str, str | None]:
    return {c: resolve(table, c) for c in concepts}


def has_concepts(table: Table, concepts: Iterable[str]) -> bool:
    """True si TODOS los conceptos resuelven a una columna existente."""
    return all(resolve(table, c) is not None for c in concepts)


# ---------------------------------------------------------------------------
# Catálogos "ancla" para vistas explorer
# ---------------------------------------------------------------------------

# Catálogos GEO públicos (sin gating por permisos — DIVIPOLA es info pública trivial)
GEO_PUBLIC_CATALOGS = {
    "divipola_departamentos",
    "divipola_municipios",
    "divipola_centros_poblados",
    "codigos_postales",
    "vias_invias",
}

# Catálogos REPS que conforman la vista 360 de un prestador
REPS_PRESTADOR_360 = {
    "habilitados": "reps_habilitados",
    "prestadores": "reps_prestadores",
    "sedes": "reps_sedes",
    "servicios": "reps_servicios",
    "capacidades": "reps_capacidades",
    "sanciones": "reps_sanciones",
    "medidas_seguridad": "reps_medidas_seguridad",
}

# Catálogos clínicos top-level (cada uno con su propia vista 360 ligera)
CLINICAL_TOP = {
    "cie10": "Diagnósticos CIE-10",
    "cups": "Procedimientos CUPS",
    "ium_medicamentos": "Medicamentos IUM",
    "procedimientos_pbs": "Procedimientos PBS",
    "medicamentos_pbs": "Medicamentos PBS",
    "eapb_codigos": "EAPB (aseguradoras)",
    "glosario_medico": "Glosario médico",
}

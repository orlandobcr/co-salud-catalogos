"""Capa REST API sobre los catálogos sincronizados.

Expone los datos persistidos en la DB (la misma a la que apunta el sync)
con autenticación bearer JWT, usuarios + contraseñas y permisos por
catálogo. Documentación OpenAPI/Swagger se filtra dinámicamente según
los permisos del usuario logueado.

Levantar:
    uvicorn sync_catalogos.api.main:app --host 0.0.0.0 --port 8000

Bootstrap inicial (crea tablas + super_admin):
    python -m sync_catalogos.api.bootstrap
"""

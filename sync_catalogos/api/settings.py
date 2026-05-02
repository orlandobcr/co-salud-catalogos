"""Configuración de la API leída de variables de entorno."""

from __future__ import annotations

import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings de la API. Variables de entorno con prefijo `SALUD_API_`."""

    model_config = SettingsConfigDict(
        env_prefix="SALUD_API_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # DB destino — debe apuntar al mismo motor donde corre el sync.
    db_url: str = Field(
        default="sqlite:///./salud.db",
        description="URL SQLAlchemy de la DB. Ej: postgresql+psycopg://u:p@h:5432/salud",
    )

    # JWT
    jwt_secret: str = Field(
        default="",
        description="Secreto HMAC para firmar tokens. Generar con: openssl rand -hex 32",
    )
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60 * 8       # 8 horas

    # Bind
    bind_host: str = "0.0.0.0"
    bind_port: int = 8000

    # CORS
    cors_origins: list[str] = ["*"]

    # Comportamiento
    page_size_default: int = 100
    page_size_max: int = 5000


def load() -> Settings:
    s = Settings()
    if not s.jwt_secret:
        raise RuntimeError(
            "SALUD_API_JWT_SECRET no está seteada. Generar con:\n"
            "  openssl rand -hex 32\n"
            "y exportar como SALUD_API_JWT_SECRET=<valor>"
        )
    return s


# Cache (lazy) — se inicializa al primer acceso
_SETTINGS: Settings | None = None


def settings() -> Settings:
    global _SETTINGS
    if _SETTINGS is None:
        _SETTINGS = load()
    return _SETTINGS

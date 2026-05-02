"""Modelos: tablas SQLAlchemy + schemas Pydantic.

Tablas (creadas por bootstrap, no por sync):
    api_users
    api_user_permissions
    api_audit_log
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
)


api_metadata = MetaData()


api_users = Table(
    "api_users", api_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(80), unique=True, nullable=False, index=True),
    Column("password_hash", String(255), nullable=False),
    Column("role", String(20), nullable=False),  # 'super_admin' | 'regular'
    Column("is_active", Boolean, default=True, nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("updated_at", DateTime(timezone=True), nullable=False),
)

api_user_permissions = Table(
    "api_user_permissions", api_metadata,
    Column("user_id", Integer, ForeignKey("api_users.id", ondelete="CASCADE"), nullable=False),
    Column("catalog_name", String(120), nullable=False),
    Column("granted_at", DateTime(timezone=True), nullable=False),
    PrimaryKeyConstraint("user_id", "catalog_name"),
)

api_audit_log = Table(
    "api_audit_log", api_metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("ts", DateTime(timezone=True), nullable=False, index=True),
    Column("user_id", Integer, nullable=True),
    Column("username", String(80), nullable=True),
    Column("method", String(10), nullable=False),
    Column("path", String(255), nullable=False),
    Column("status_code", Integer, nullable=False),
    Column("ip", String(64)),
    Column("notes", Text),
)


# ---------------------------------------------------------------------------
# Pydantic schemas (request / response)
# ---------------------------------------------------------------------------

UserRole = Literal["super_admin", "regular"]


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = Field(..., description="Segundos hasta expiración")
    role: UserRole
    username: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime
    permissions: list[str] = Field(
        default_factory=list,
        description="Catálogos permitidos. Vacío para super_admin (acceso total implícito).",
    )

    model_config = ConfigDict(from_attributes=True)


class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=80)
    password: str = Field(..., min_length=8)
    role: UserRole = "regular"
    permissions: list[str] = Field(
        default_factory=list,
        description="Lista de catalog names. Aplica solo a regular users.",
    )


class UserUpdateRequest(BaseModel):
    password: str | None = Field(None, min_length=8)
    role: UserRole | None = None
    is_active: bool | None = None


class PermissionGrantRequest(BaseModel):
    catalog_names: list[str] = Field(..., min_length=1)


class CatalogSummary(BaseModel):
    name: str
    source: str
    source_url: str | None = None
    row_count: int | None = None
    last_synced: datetime | None = None
    table_name: str | None = None


class CatalogDetail(CatalogSummary):
    description: str | None = None
    license: str | None = None
    version: str | None = None
    sha256: str | None = None
    notes: str | None = None
    schema_: list[dict] | None = Field(None, alias="schema")

    model_config = ConfigDict(populate_by_name=True)


class EntriesPage(BaseModel):
    catalog: str
    total: int
    limit: int
    offset: int
    entries: list[dict]


class AuditLogEntry(BaseModel):
    id: int
    ts: datetime
    username: str | None
    method: str
    path: str
    status_code: int
    ip: str | None = None
    notes: str | None = None

"""Endpoints de administración (solo super_admin)."""

from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy import delete, insert, select, update

from ..auth import (
    CurrentUser,
    hash_password,
    require_super_admin,
)
from ..db import all_catalog_names, catalog_exists
from ..models import (
    AuditLogEntry,
    PermissionGrantRequest,
    UserCreateRequest,
    UserOut,
    UserUpdateRequest,
    api_audit_log,
    api_user_permissions,
    api_users,
)


router = APIRouter(prefix="/api/v1/admin", tags=["admin (super_admin only)"])


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

@router.get("/users", response_model=list[UserOut], summary="Lista todos los usuarios")
def list_users(request: Request, _: CurrentUser = Depends(require_super_admin)):
    engine = request.app.state.engine
    out = []
    with engine.connect() as conn:
        rows = conn.execute(select(api_users).order_by(api_users.c.id)).all()
        for u in rows:
            perms = conn.execute(
                select(api_user_permissions.c.catalog_name)
                .where(api_user_permissions.c.user_id == u.id)
                .order_by(api_user_permissions.c.catalog_name)
            ).all()
            out.append(UserOut(
                id=u.id, username=u.username, role=u.role, is_active=u.is_active,
                created_at=u.created_at, updated_at=u.updated_at,
                permissions=[p.catalog_name for p in perms],
            ))
    return out


@router.post("/users", response_model=UserOut, status_code=201, summary="Crea un usuario")
def create_user(
    req: UserCreateRequest,
    request: Request,
    _: CurrentUser = Depends(require_super_admin),
):
    engine = request.app.state.engine
    now = datetime.now(UTC)
    with engine.begin() as conn:
        existing = conn.execute(
            select(api_users.c.id).where(api_users.c.username == req.username)
        ).first()
        if existing:
            raise HTTPException(status_code=409, detail=f"Usuario '{req.username}' ya existe")

        # Validar catálogos solicitados
        valid = set(all_catalog_names(engine))
        invalid = [c for c in req.permissions if c not in valid]
        if invalid:
            raise HTTPException(
                status_code=400,
                detail=f"Catálogos no encontrados en la DB: {invalid}",
            )

        result = conn.execute(insert(api_users).values(
            username=req.username,
            password_hash=hash_password(req.password),
            role=req.role,
            is_active=True,
            created_at=now,
            updated_at=now,
        ))
        user_id = result.inserted_primary_key[0]
        if req.role == "regular" and req.permissions:
            conn.execute(insert(api_user_permissions), [
                {"user_id": user_id, "catalog_name": c, "granted_at": now}
                for c in req.permissions
            ])
    return UserOut(
        id=user_id, username=req.username, role=req.role, is_active=True,
        created_at=now, updated_at=now,
        permissions=req.permissions if req.role == "regular" else [],
    )


@router.patch("/users/{user_id}", response_model=UserOut, summary="Actualiza usuario (rol, password, activo)")
def update_user(
    user_id: int,
    req: UserUpdateRequest,
    request: Request,
    _: CurrentUser = Depends(require_super_admin),
):
    engine = request.app.state.engine
    now = datetime.now(UTC)
    updates: dict = {"updated_at": now}
    if req.password is not None:
        updates["password_hash"] = hash_password(req.password)
    if req.role is not None:
        updates["role"] = req.role
    if req.is_active is not None:
        updates["is_active"] = req.is_active

    with engine.begin() as conn:
        existing = conn.execute(select(api_users).where(api_users.c.id == user_id)).first()
        if not existing:
            raise HTTPException(status_code=404, detail="Usuario no existe")
        conn.execute(update(api_users).where(api_users.c.id == user_id).values(**updates))
        u = conn.execute(select(api_users).where(api_users.c.id == user_id)).first()
        perms = conn.execute(
            select(api_user_permissions.c.catalog_name)
            .where(api_user_permissions.c.user_id == user_id)
        ).all()
    return UserOut(
        id=u.id, username=u.username, role=u.role, is_active=u.is_active,
        created_at=u.created_at, updated_at=u.updated_at,
        permissions=[p.catalog_name for p in perms],
    )


@router.delete("/users/{user_id}", status_code=204, summary="Desactiva un usuario (soft delete)")
def deactivate_user(user_id: int, request: Request, _: CurrentUser = Depends(require_super_admin)):
    engine = request.app.state.engine
    with engine.begin() as conn:
        existing = conn.execute(select(api_users.c.id).where(api_users.c.id == user_id)).first()
        if not existing:
            raise HTTPException(status_code=404, detail="Usuario no existe")
        conn.execute(
            update(api_users).where(api_users.c.id == user_id)
            .values(is_active=False, updated_at=datetime.now(UTC))
        )
    return None


# ---------------------------------------------------------------------------
# Permissions
# ---------------------------------------------------------------------------

@router.post("/users/{user_id}/permissions", response_model=UserOut, summary="Otorga permisos a catálogos")
def grant_permissions(
    user_id: int,
    req: PermissionGrantRequest,
    request: Request,
    _: CurrentUser = Depends(require_super_admin),
):
    engine = request.app.state.engine
    valid = set(all_catalog_names(engine))
    invalid = [c for c in req.catalog_names if c not in valid]
    if invalid:
        raise HTTPException(status_code=400, detail=f"Catálogos no encontrados: {invalid}")

    now = datetime.now(UTC)
    with engine.begin() as conn:
        u = conn.execute(select(api_users).where(api_users.c.id == user_id)).first()
        if not u:
            raise HTTPException(status_code=404, detail="Usuario no existe")
        # Insert ignorando duplicados (delete + insert simple)
        for c in req.catalog_names:
            conn.execute(
                delete(api_user_permissions)
                .where(api_user_permissions.c.user_id == user_id)
                .where(api_user_permissions.c.catalog_name == c)
            )
        conn.execute(insert(api_user_permissions), [
            {"user_id": user_id, "catalog_name": c, "granted_at": now}
            for c in req.catalog_names
        ])
        perms = conn.execute(
            select(api_user_permissions.c.catalog_name)
            .where(api_user_permissions.c.user_id == user_id)
            .order_by(api_user_permissions.c.catalog_name)
        ).all()
    return UserOut(
        id=u.id, username=u.username, role=u.role, is_active=u.is_active,
        created_at=u.created_at, updated_at=u.updated_at,
        permissions=[p.catalog_name for p in perms],
    )


@router.delete(
    "/users/{user_id}/permissions/{catalog_name}",
    status_code=204,
    summary="Revoca permiso a un catálogo",
)
def revoke_permission(
    user_id: int, catalog_name: str, request: Request,
    _: CurrentUser = Depends(require_super_admin),
):
    engine = request.app.state.engine
    with engine.begin() as conn:
        conn.execute(
            delete(api_user_permissions)
            .where(api_user_permissions.c.user_id == user_id)
            .where(api_user_permissions.c.catalog_name == catalog_name)
        )
    return None


# ---------------------------------------------------------------------------
# Catalog options (helper para UI)
# ---------------------------------------------------------------------------

@router.get(
    "/catalog-options",
    response_model=list[str],
    summary="Lista todos los catálogos sincronizados (para popular formularios de permisos)",
)
def list_catalog_options(request: Request, _: CurrentUser = Depends(require_super_admin)):
    return all_catalog_names(request.app.state.engine)


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------

@router.get("/audit", response_model=list[AuditLogEntry], summary="Log de auditoría reciente")
def get_audit(
    request: Request,
    limit: int = Query(default=200, ge=1, le=2000),
    _: CurrentUser = Depends(require_super_admin),
):
    engine = request.app.state.engine
    with engine.connect() as conn:
        rows = conn.execute(
            select(api_audit_log).order_by(api_audit_log.c.id.desc()).limit(limit)
        ).all()
    return [
        AuditLogEntry(
            id=r.id, ts=r.ts, username=r.username,
            method=r.method, path=r.path, status_code=r.status_code,
            ip=r.ip, notes=r.notes,
        )
        for r in rows
    ]

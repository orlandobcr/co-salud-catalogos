"""Endpoints de autenticación."""

from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select, update

from ..auth import (
    CurrentUser,
    create_token,
    get_current_user,
    verify_password,
)
from ..models import (
    LoginRequest,
    TokenResponse,
    UserOut,
    api_user_permissions,
    api_users,
)


router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse, summary="Login con username + contraseña")
def login(req: LoginRequest, request: Request):
    engine = request.app.state.engine
    with engine.begin() as conn:
        row = conn.execute(
            select(
                api_users.c.id, api_users.c.username, api_users.c.password_hash,
                api_users.c.role, api_users.c.is_active,
            ).where(api_users.c.username == req.username)
        ).first()
        if not row or not row.is_active:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        if not verify_password(req.password, row.password_hash):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        # Update updated_at (touch)
        conn.execute(
            update(api_users)
            .where(api_users.c.id == row.id)
            .values(updated_at=datetime.now(UTC))
        )
    token, expires_in = create_token(row.username, row.id, row.role)
    return TokenResponse(
        access_token=token,
        expires_in=expires_in,
        role=row.role,
        username=row.username,
    )


@router.get("/me", response_model=UserOut, summary="Datos del usuario logueado + permisos")
def me(request: Request, user: CurrentUser = Depends(get_current_user)):
    engine = request.app.state.engine
    with engine.connect() as conn:
        row = conn.execute(
            select(api_users).where(api_users.c.id == user.id)
        ).first()
        perms = conn.execute(
            select(api_user_permissions.c.catalog_name)
            .where(api_user_permissions.c.user_id == user.id)
            .order_by(api_user_permissions.c.catalog_name)
        ).all()
    if not row:
        raise HTTPException(status_code=404, detail="Usuario no existe")
    return UserOut(
        id=row.id,
        username=row.username,
        role=row.role,
        is_active=row.is_active,
        created_at=row.created_at,
        updated_at=row.updated_at,
        permissions=[p.catalog_name for p in perms],
    )

"""Autenticación: hashing de contraseñas + JWT bearer + dependencies FastAPI."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Optional

import bcrypt
import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.engine import Engine

from .models import api_user_permissions, api_users
from .settings import settings

# bcrypt directo (sin passlib) — más simple y sin problemas en Python 3.14+

bearer_scheme = HTTPBearer(auto_error=False)

# bcrypt limita a 72 bytes — truncamos consistentemente para evitar errores
_BCRYPT_MAX = 72


def _truncate(plain: str) -> bytes:
    """Truncar a 72 bytes (límite bcrypt). Determinista y consistente."""
    return plain.encode("utf-8")[:_BCRYPT_MAX]


def hash_password(plain: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(_truncate(plain), salt).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(_truncate(plain), hashed.encode("utf-8"))
    except Exception:
        return False


def create_token(username: str, user_id: int, role: str) -> tuple[str, int]:
    """Devuelve (token, expires_in_seconds)."""
    s = settings()
    now = datetime.now(UTC)
    expire_at = now + timedelta(minutes=s.jwt_expire_minutes)
    payload = {
        "sub": username,
        "uid": user_id,
        "role": role,
        "iat": int(now.timestamp()),
        "exp": int(expire_at.timestamp()),
    }
    token = jwt.encode(payload, s.jwt_secret, algorithm=s.jwt_algorithm)
    return token, s.jwt_expire_minutes * 60


def decode_token(token: str) -> dict:
    s = settings()
    try:
        return jwt.decode(token, s.jwt_secret, algorithms=[s.jwt_algorithm])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Token inválido: {e}")


# ---------------------------------------------------------------------------
# Current user model
# ---------------------------------------------------------------------------

class CurrentUser:
    """Inyectado en handlers vía Depends(get_current_user)."""

    def __init__(self, user_id: int, username: str, role: str, permissions: set[str]):
        self.id = user_id
        self.username = username
        self.role = role
        self.permissions = permissions  # set de catalog names

    @property
    def is_super_admin(self) -> bool:
        return self.role == "super_admin"

    def can_access(self, catalog_name: str) -> bool:
        return self.is_super_admin or catalog_name in self.permissions


# ---------------------------------------------------------------------------
# Dependencies (FastAPI)
# ---------------------------------------------------------------------------

def get_engine_dep(request: Request) -> Engine:
    """Engine compartido vía app.state.engine (set en main.py lifespan)."""
    return request.app.state.engine


def _load_user_from_db(engine: Engine, user_id: int) -> Optional[dict]:
    with engine.connect() as conn:
        row = conn.execute(
            select(
                api_users.c.id, api_users.c.username, api_users.c.role,
                api_users.c.is_active,
            ).where(api_users.c.id == user_id)
        ).first()
        if not row or not row.is_active:
            return None
        perms = conn.execute(
            select(api_user_permissions.c.catalog_name)
            .where(api_user_permissions.c.user_id == user_id)
        ).all()
    return {
        "id": row.id,
        "username": row.username,
        "role": row.role,
        "permissions": {p.catalog_name for p in perms},
    }


def get_current_user(
    request: Request,
    creds: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> CurrentUser:
    """Resuelve el usuario actual desde el bearer token. 401 si inválido."""
    if creds is None or creds.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer token requerido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    payload = decode_token(creds.credentials)
    user_id = payload.get("uid")
    if not isinstance(user_id, int):
        raise HTTPException(status_code=401, detail="Token sin uid válido")
    engine = request.app.state.engine
    info = _load_user_from_db(engine, user_id)
    if info is None:
        raise HTTPException(status_code=401, detail="Usuario inactivo o no existe")
    return CurrentUser(
        user_id=info["id"],
        username=info["username"],
        role=info["role"],
        permissions=info["permissions"],
    )


def get_current_user_optional(
    request: Request,
    creds: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> CurrentUser | None:
    """Igual que get_current_user pero devuelve None si no hay token (no 401)."""
    if creds is None or creds.scheme.lower() != "bearer":
        return None
    try:
        return get_current_user(request, creds)
    except HTTPException:
        return None


def require_super_admin(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
    if not user.is_super_admin:
        raise HTTPException(status_code=403, detail="Solo super_admin puede acceder")
    return user


def require_catalog_access(catalog_name: str):
    """Factory de dependency que valida acceso a un catálogo específico."""

    def _check(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if not user.can_access(catalog_name):
            raise HTTPException(
                status_code=403,
                detail=f"Sin permiso para el catálogo '{catalog_name}'",
            )
        return user

    return _check

"""Bootstrap CLI: crea las tablas de la API y opcionalmente un super_admin.

Uso:
    python -m sync_catalogos.api.bootstrap
    python -m sync_catalogos.api.bootstrap --create-superadmin admin
"""

from __future__ import annotations

import argparse
import getpass
import sys
from datetime import datetime, timezone

from sqlalchemy import create_engine, insert, select

from .._envfile import load_env
from .auth import hash_password
from .models import api_metadata, api_users
from .settings import settings


def main(argv: list[str] | None = None) -> int:
    load_env()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db-url", help="Override SALUD_API_DB_URL")
    ap.add_argument("--create-superadmin", metavar="USERNAME", help="Crea un super_admin con ese username")
    ap.add_argument("--password", help="Password (si no se da, se prompt)")
    args = ap.parse_args(argv)

    s = settings()
    db_url = args.db_url or s.db_url
    print(f"DB: {db_url.split('@')[-1]}")

    engine = create_engine(db_url, future=True)
    print("Creando tablas API (idempotente)...")
    api_metadata.create_all(engine)
    print("  ✓ api_users, api_user_permissions, api_audit_log")

    if args.create_superadmin:
        username = args.create_superadmin
        password = args.password
        if not password:
            password = getpass.getpass(f"Password para super_admin '{username}': ")
            confirm = getpass.getpass("Repetir: ")
            if password != confirm:
                print("Las contraseñas no coinciden", file=sys.stderr)
                return 1
        if len(password) < 8:
            print("Password debe tener al menos 8 caracteres", file=sys.stderr)
            return 1

        with engine.begin() as conn:
            existing = conn.execute(
                select(api_users.c.id).where(api_users.c.username == username)
            ).first()
            if existing:
                print(f"Usuario '{username}' ya existe (id={existing.id})", file=sys.stderr)
                return 1
            now = datetime.now(timezone.utc)
            r = conn.execute(insert(api_users).values(
                username=username,
                password_hash=hash_password(password),
                role="super_admin",
                is_active=True,
                created_at=now,
                updated_at=now,
            ))
        print(f"  ✓ super_admin '{username}' creado (id={r.inserted_primary_key[0]})")
        print()
        print("Levantar la API:")
        print("    uvicorn sync_catalogos.api.main:app --host 0.0.0.0 --port 8000")
        print(f"Login: POST /auth/login con {{ \"username\": \"{username}\", \"password\": \"...\" }}")
    else:
        # Si no hay ningún user, recordar
        with engine.connect() as conn:
            count = conn.execute(select(api_users.c.id)).all()
        if not count:
            print()
            print("⚠ No hay ningún usuario. Crear el primer super_admin:")
            print("    python -m sync_catalogos.api.bootstrap --create-superadmin admin")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Diagnóstico del pool de proxies — útil para verificar setup antes de un sync.

Uso:
    python -m sync_catalogos.proxy_check

Salida (humana):
    - Estado de configuración env (PROXY_ENABLED, provider activo, kinds)
    - Si hay 2captcha key: balance, IPs whitelisted, IP pública actual
    - Pool refrescado: cuántos proxies, distribución por protocolo
    - Test de conectividad: cada protocolo contra httpbin.org/ip
"""

from __future__ import annotations

import os
import sys
import time
from collections import Counter

import httpx

from ._envfile import load_env
from .proxy import (
    HttpProvider,
    StaticProvider,
    TwoCaptchaProvider,
    _make_provider,
    _scheme_of,
    get_pool,
    should_use_proxy_for_kind,
)


def _print(label: str, value, indent: int = 2) -> None:
    print(f"{' ' * indent}{label:30s} {value}")


def main() -> int:
    load_env()
    print("=" * 70)
    print("Diagnóstico del pool de proxies")
    print("=" * 70)

    # 1. Config env
    print("\n[1] Configuración de entorno")
    _print("PROXY_ENABLED", os.environ.get("PROXY_ENABLED", "(unset)"))
    _print("PROXY_USE_FOR_KINDS", os.environ.get("PROXY_USE_FOR_KINDS", "(unset → defaults)"))
    _print("PROXY_PROTOCOL", os.environ.get("PROXY_PROTOCOL", "(unset → all 3)"))
    _print("PROXY_COUNTRY", os.environ.get("PROXY_COUNTRY", "(unset → mix)"))
    _print("PROXY_POOL_SIZE", os.environ.get("PROXY_POOL_SIZE", "10"))

    # 2. Switch por kind
    print("\n[2] Decisión por kind (use_proxy)")
    for k in ("socrata", "reps_export", "sispro_aspx"):
        _print(k, should_use_proxy_for_kind(k))

    # 3. Provider activo
    provider = _make_provider()
    print("\n[3] Provider activo")
    if provider is None:
        _print("provider", "(ninguno) — todo va directo")
        return 0
    _print("provider", provider.__class__.__name__)

    # 4. Diagnóstico específico de 2captcha
    if isinstance(provider, TwoCaptchaProvider):
        print("\n[4] 2captcha — diagnóstico de cuenta")
        try:
            with httpx.Client(timeout=15) as c:
                r = c.get("https://api.2captcha.com/proxy", params={"key": provider.api_key})
                data = r.json().get("data", {})
            _print("username", data.get("username"))
            _print("status", data.get("status"))
            _print("total_flow_GB", data.get("total_flow"))
            _print("traffic_remaining", f"{data.get('last_flow', 0):.1f} GB")
            ip_white = data.get("ip_white") or []
            _print("ip_white", ip_white if ip_white else "(vacío — añade tu IP en https://2captcha.com/setting/ip-whitelist)")

            # Mi IP pública
            try:
                me = httpx.get("https://api.ipify.org", timeout=10).text
                _print("my_public_ip", me)
                _print("ip_match", "✓" if me in ip_white else f"⚠ tu IP {me} NO está whitelisted")
            except Exception:
                pass
        except Exception as e:
            _print("ERR", str(e))
    elif isinstance(provider, StaticProvider):
        print("\n[4] StaticProvider — lista PROXY_LIST")
        urls = provider.fetch()
        _print("URLs configuradas", len(urls))
    elif isinstance(provider, HttpProvider):
        print("\n[4] HttpProvider — endpoint PROXY_LIST_URL")
        _print("URL", provider.url)

    # 5. Pool
    print("\n[5] Pool refrescado")
    pool = get_pool()
    pool._maybe_refresh()
    _print("is_active", pool.is_active())
    _print("proxies", len(pool._proxies))
    if pool._proxies:
        protos = Counter(_scheme_of(p.url) for p in pool._proxies)
        _print("por protocolo", dict(protos))

    # 6. Connectivity test
    if pool._proxies:
        print("\n[6] Test de conectividad (1 proxy de cada protocolo)")
        seen = set()
        for p in pool._proxies:
            proto = _scheme_of(p.url)
            if proto in seen:
                continue
            seen.add(proto)
            t0 = time.time()
            try:
                r = httpx.get("http://httpbin.org/ip", proxy=p.url, timeout=10)
                _print(f"{proto:7s}", f"HTTP {r.status_code} ({time.time()-t0:.1f}s)  {r.text[:60].strip()}")
            except Exception as e:
                _print(f"{proto:7s}", f"ERR {type(e).__name__}: {str(e)[:80]}")

    print()
    print("=" * 70)
    print("Listo. Si los proxies fallan, el sync sigue funcionando vía fallback")
    print("automático a directo (overhead despreciable después de cooldown).")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

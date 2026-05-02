"""Pool de proxies paramétrico con fallback automático a conexión directa.

Diseño:

- **Providers pluggables** — el pool no asume proveedor: lo configura via env.
  Soportados out-of-the-box:
    1. `StaticProvider` — lista plana en `PROXY_LIST` (CSV de URLs).
       Ej: `PROXY_LIST="http://u:p@ip1:8000,http://u:p@ip2:8000"`
    2. `HttpProvider` — endpoint propio en `PROXY_LIST_URL`. Debe devolver
       una lista JSON (`["http://...", ...]`) o texto plano (1 URL por línea).
       Útil para integrar con BrightData, Smartproxy, IPRoyal, ScraperAPI, etc.
- **Refresh periódico**: cada N minutos (default 30) re-pregunta al provider;
  IPs nuevas entran al pool, las que desaparecen se descartan.
- **Health tracking**: cada IP tiene contador de fallos. Tras `fail_threshold`
  consecutivos, entra en `cooldown_seconds` (default 5 min).
- **Fallback automático**: si todos los proxies fallan en una request, se
  reintenta directo. Si la directa también falla, se propaga el error.
  El sync NUNCA se bloquea por problemas de proxy — peor caso = sync directo.
- **Sticky por host**: misma corrida reusa el mismo proxy para mantener
  cookies de sesión ASP.NET.

Punto de entrada único: `make_http_client(target_host)`.

Notas:
- El servicio 2captcha (`TWOCAPTCHA_API_KEY`) NO provee proxies — es un
  CAPTCHA solver. Ver `captcha.py` para ese uso.
"""

from __future__ import annotations

import logging
import os
import random
import threading
import time
from dataclasses import dataclass
from typing import Iterable, Protocol

import httpx

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers env
# ---------------------------------------------------------------------------

def _env_bool(name: str, default: bool = False) -> bool:
    v = os.environ.get(name, "").strip().lower()
    if not v:
        return default
    return v in ("1", "true", "yes", "y", "on")


def _env_int(name: str, default: int) -> int:
    v = os.environ.get(name, "").strip()
    if not v:
        return default
    try:
        return int(v)
    except ValueError:
        return default


# ---------------------------------------------------------------------------
# Providers
# ---------------------------------------------------------------------------

class ProxyProvider(Protocol):
    """Interfaz para fuentes de proxies. Cada provider devuelve URLs listas
    para httpx (`http://[user:pass@]host:port` o `socks5://...`)."""

    def fetch(self) -> list[str]: ...


class StaticProvider:
    """Lee la lista de `PROXY_LIST` (variable de entorno, CSV)."""

    def __init__(self, raw: str) -> None:
        self.raw = raw

    def fetch(self) -> list[str]:
        if not self.raw:
            return []
        return [u.strip() for u in self.raw.split(",") if u.strip()]


class HttpProvider:
    """Pide la lista a un endpoint HTTP propio (`PROXY_LIST_URL`).

    El endpoint debe devolver:
      - JSON: lista de strings (`["http://...", ...]`)
        o lista de objetos con campos `host, port, user, password, protocol`.
      - O texto plano: una URL por línea.
    """

    def __init__(self, url: str, *, timeout: float = 15.0) -> None:
        self.url = url
        self.timeout = timeout

    def fetch(self) -> list[str]:
        try:
            with httpx.Client(timeout=self.timeout) as c:
                r = c.get(self.url)
                r.raise_for_status()
                ct = r.headers.get("content-type", "")
                if "json" in ct:
                    data = r.json()
                    return _normalize_json_proxies(data)
                # Plain text fallback
                return [l.strip() for l in r.text.splitlines() if l.strip() and not l.startswith("#")]
        except Exception as e:
            log.warning("proxy.http_provider_failed", extra={"url": self.url, "error": str(e)})
            return []


def _normalize_json_proxies(data) -> list[str]:
    out: list[str] = []
    items = data if isinstance(data, list) else (data.get("proxies") or data.get("list") or [])
    for item in items:
        if isinstance(item, str):
            out.append(item if "://" in item else f"http://{item}")
        elif isinstance(item, dict):
            host = item.get("ip") or item.get("host") or item.get("address")
            port = item.get("port")
            if not (host and port):
                continue
            user = item.get("user") or item.get("username") or item.get("login")
            pwd = item.get("password") or item.get("pass")
            proto = (item.get("protocol") or item.get("proto") or "http").lower()
            if user and pwd:
                out.append(f"{proto}://{user}:{pwd}@{host}:{port}")
            else:
                out.append(f"{proto}://{host}:{port}")
    return out


class TwoCaptchaProvider:
    """2captcha residential proxy network (https://2captcha.com/proxy).

    Uso:
        export TWOCAPTCHA_API_KEY=...
        export PROXY_COUNTRY=co              # opcional, default mix
        export PROXY_PROTOCOL=http           # http | https | socks5
        export PROXY_POOL_SIZE=10            # 1..2000

    Modelo: el usuario tiene IPs whitelisted en su cuenta 2captcha
    (https://2captcha.com/setting/ip-whitelist). Por cada IP whitelisted,
    `generate_white_list_connections` devuelve N URLs `IP:PORT` autenticadas
    por whitelist (sin user/pass). Si la cuenta no tiene IPs whitelisted,
    el provider devuelve [] y el pool cae a modo directo.
    """

    BASE = "https://api.2captcha.com/proxy"

    def __init__(
        self,
        api_key: str,
        *,
        country: str = "",          # vacío = "mix" (cualquier país)
        protocols: list[str] | None = None,
        pool_size: int = 10,
        timeout: float = 15.0,
    ) -> None:
        self.api_key = api_key
        self.country = country
        # Si no se especifica, generamos en los 3 protocolos para máximo fallback
        self.protocols = protocols or ["http", "https", "socks5"]
        self.pool_size = max(1, min(2000, pool_size))
        self.timeout = timeout

    def _account_info(self, c: httpx.Client) -> dict | None:
        try:
            r = c.get(self.BASE, params={"key": self.api_key})
            r.raise_for_status()
            data = r.json()
            if data.get("status") == "OK":
                return data.get("data") or {}
        except Exception as e:
            log.warning("proxy.2captcha.account_info_failed", extra={"error": str(e)})
        return None

    def fetch(self) -> list[str]:
        with httpx.Client(timeout=self.timeout) as c:
            info = self._account_info(c)
            if info is None:
                return []
            ip_white = info.get("ip_white") or []
            if not ip_white:
                log.warning(
                    "proxy.2captcha.no_whitelist_ips",
                    extra={
                        "username": info.get("username"),
                        "hint": "Whitelist your public IP at https://2captcha.com/setting/ip-whitelist",
                    },
                )
                return []
            # Distribuye pool_size entre IPs whitelisted × protocolos
            slots_per_combo = max(1, self.pool_size // (len(ip_white) * len(self.protocols)))
            urls: list[str] = []
            for ip in ip_white:
                for protocol in self.protocols:
                    params = {
                        "key": self.api_key,
                        "ip": ip,
                        "protocol": protocol,
                        "connection_count": str(slots_per_combo),
                    }
                    if self.country:
                        params["country"] = self.country
                    try:
                        r = c.get(f"{self.BASE}/generate_white_list_connections", params=params)
                        r.raise_for_status()
                        data = r.json()
                        if data.get("status") != "OK":
                            log.warning("proxy.2captcha.generate_failed", extra={"protocol": protocol, "data": data})
                            continue
                        for ip_port in data.get("data") or []:
                            if "://" in ip_port:
                                urls.append(ip_port)
                            else:
                                urls.append(f"{protocol}://{ip_port}")
                    except Exception as e:
                        log.warning("proxy.2captcha.generate_error", extra={"ip": ip, "protocol": protocol, "error": str(e)})
                        continue
            return urls


def _make_provider() -> ProxyProvider | None:
    """Construye el provider activo según las env vars disponibles.

    Prioridad:
      1. `PROXY_LIST`            — lista plana CSV
      2. `PROXY_LIST_URL`        — endpoint propio
      3. `TWOCAPTCHA_API_KEY`    — proxy network 2captcha
    """
    static = os.environ.get("PROXY_LIST", "").strip()
    if static:
        return StaticProvider(static)
    url = os.environ.get("PROXY_LIST_URL", "").strip()
    if url:
        return HttpProvider(url)
    api_key = os.environ.get("TWOCAPTCHA_API_KEY", "").strip()
    if api_key:
        # Si PROXY_PROTOCOL está seteado, usa solo ese; si no, los 3.
        proto = os.environ.get("PROXY_PROTOCOL", "").strip().lower()
        protocols = [proto] if proto else ["http", "https", "socks5"]
        return TwoCaptchaProvider(
            api_key,
            country=os.environ.get("PROXY_COUNTRY", "").strip().lower(),
            protocols=protocols,
            pool_size=_env_int("PROXY_POOL_SIZE", 10),
        )
    return None


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ProxyConfig:
    enabled: bool = False
    refresh_minutes: int = 30
    fail_threshold: int = 3
    cooldown_seconds: int = 300
    request_timeout: float = 30.0
    max_attempts: int = 6          # cuántos proxies probar antes de fallback a directo

    @classmethod
    def from_env(cls) -> "ProxyConfig":
        return cls(
            enabled=_env_bool("PROXY_ENABLED", False),
            refresh_minutes=_env_int("PROXY_REFRESH_MINUTES", 30),
            fail_threshold=_env_int("PROXY_FAIL_THRESHOLD", 3),
            cooldown_seconds=_env_int("PROXY_COOLDOWN_SECONDS", 300),
            max_attempts=_env_int("PROXY_MAX_ATTEMPTS", 6),
        )


# ---------------------------------------------------------------------------
# Health tracking
# ---------------------------------------------------------------------------

@dataclass
class ProxyEntry:
    url: str
    fail_count: int = 0
    cooldown_until: float = 0.0
    last_used: float = 0.0

    def is_healthy(self) -> bool:
        return time.time() >= self.cooldown_until


# ---------------------------------------------------------------------------
# Pool
# ---------------------------------------------------------------------------

class ProxyPool:
    def __init__(
        self,
        config: ProxyConfig | None = None,
        provider: ProxyProvider | None = None,
    ) -> None:
        self.config = config or ProxyConfig.from_env()
        self.provider = provider if provider is not None else _make_provider()
        self._lock = threading.RLock()
        self._proxies: list[ProxyEntry] = []
        self._last_refresh: float = 0.0
        self._stickiness: dict[str, ProxyEntry] = {}

    def is_active(self) -> bool:
        """True solo si está habilitado Y hay un provider configurado."""
        return self.config.enabled and self.provider is not None

    def get_for(self, target_host: str) -> str | None:
        """URL del proxy para un host (sticky), o None si no hay sano / no activo."""
        if not self.is_active():
            return None
        self._maybe_refresh()
        with self._lock:
            sticky = self._stickiness.get(target_host)
            if sticky is not None and sticky.is_healthy():
                sticky.last_used = time.time()
                return sticky.url
            healthy = [p for p in self._proxies if p.is_healthy()]
            if not healthy:
                return None
            chosen = random.choice(healthy)
            self._stickiness[target_host] = chosen
            chosen.last_used = time.time()
            return chosen.url

    def healthy_proxies(self, exclude: set[str] | None = None) -> list[str]:
        """Lista de URLs de proxies sanos, excluyendo los del set (ya intentados)."""
        if not self.is_active():
            return []
        self._maybe_refresh()
        excl = exclude or set()
        with self._lock:
            return [p.url for p in self._proxies if p.is_healthy() and p.url not in excl]

    def clear_stickiness(self, target_host: str) -> None:
        with self._lock:
            self._stickiness.pop(target_host, None)

    def report_failure(self, proxy_url: str | None) -> None:
        if not proxy_url:
            return
        with self._lock:
            for p in self._proxies:
                if p.url == proxy_url:
                    p.fail_count += 1
                    if p.fail_count >= self.config.fail_threshold:
                        p.cooldown_until = time.time() + self.config.cooldown_seconds
                        log.info("proxy.unhealthy", extra={"proxy": _safe(proxy_url), "cooldown_s": self.config.cooldown_seconds})
                    return

    def report_success(self, proxy_url: str | None) -> None:
        if not proxy_url:
            return
        with self._lock:
            for p in self._proxies:
                if p.url == proxy_url:
                    p.fail_count = 0
                    return

    def _maybe_refresh(self) -> None:
        now = time.time()
        period = max(60.0, self.config.refresh_minutes * 60)
        with self._lock:
            if not self._proxies or (now - self._last_refresh) > period:
                self._refresh()

    def _refresh(self) -> None:
        urls = list(self.provider.fetch()) if self.provider else []
        if not urls:
            log.warning("proxy.refresh_empty")
            self._proxies = []
            self._stickiness.clear()
            self._last_refresh = time.time()
            return
        existing = {p.url: p for p in self._proxies}
        self._proxies = [existing.get(u, ProxyEntry(url=u)) for u in urls]
        valid = {p.url for p in self._proxies}
        self._stickiness = {h: p for h, p in self._stickiness.items() if p.url in valid}
        self._last_refresh = time.time()
        log.info("proxy.refreshed", extra={"count": len(self._proxies)})


def _safe(url: str) -> str:
    """Oculta credenciales en logs."""
    if "@" in url and "://" in url:
        scheme, rest = url.split("://", 1)
        _, host = rest.split("@", 1)
        return f"{scheme}://***@{host}"
    return url


def _scheme_of(url: str) -> str:
    """Devuelve el scheme de una URL (http, https, socks5)."""
    return url.split("://", 1)[0].lower() if "://" in url else "http"


def _order_by_protocol_diversity(urls: list[str], failed_protocols: set[str]) -> list[str]:
    """Reordena las URLs preferiendo protocolos que NO han fallado todavía.

    Estrategia round-robin por protocolo:
      [http1, https1, socks5_1, http2, https2, socks5_2, ...]
    Esto agota distintos protocolos antes de repetir el mismo.
    """
    by_proto: dict[str, list[str]] = {}
    for u in urls:
        by_proto.setdefault(_scheme_of(u), []).append(u)
    # Protocolos que aún no han fallado primero, después los que ya fallaron
    proto_order = sorted(by_proto.keys(), key=lambda p: (p in failed_protocols, p))
    out: list[str] = []
    while any(by_proto[p] for p in proto_order):
        for p in proto_order:
            if by_proto[p]:
                out.append(by_proto[p].pop(0))
    return out


# ---------------------------------------------------------------------------
# HTTP client wrapper
# ---------------------------------------------------------------------------

_PROXY_ERROR_TYPES = (
    httpx.ConnectError,
    httpx.ConnectTimeout,
    httpx.ReadTimeout,
    httpx.RemoteProtocolError,
    httpx.ProxyError,
)


class HttpClient:
    """`httpx.Client`-like façade con retry, proxy rotation y fallback a direct.

    Si el pool no está activo, se comporta como un httpx.Client estándar.
    Mantiene un `httpx.Cookies` interno persistente entre requests
    (necesario para session cookies ASP.NET de REPS / SISPRO).
    """

    def __init__(
        self,
        target_host: str,
        *,
        pool: ProxyPool | None = None,
        timeout: float = 60.0,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.target_host = target_host
        self.pool = pool
        self.timeout = timeout
        self.headers = headers or {}
        self._cookies = httpx.Cookies()
        self._direct_only = pool is None or not pool.is_active()
        self._max_attempts = pool.config.max_attempts if (pool is not None) else 0

    @property
    def cookies(self) -> httpx.Cookies:
        return self._cookies

    def _build_client(self, proxy: str | None) -> httpx.Client:
        return httpx.Client(
            timeout=self.timeout,
            headers=self.headers,
            cookies=self._cookies,
            follow_redirects=True,
            proxy=proxy,
        )

    def _execute(self, proxy: str | None, method: str, url: str, **kwargs) -> httpx.Response:
        with self._build_client(proxy) as c:
            r = c.request(method, url, **kwargs)
            self._cookies.update(r.cookies)
            return r

    def request(self, method: str, url: str, **kwargs) -> httpx.Response:
        if self._direct_only:
            return self._execute(None, method, url, **kwargs)

        # Estrategia: intentar TODOS los proxies sanos del pool antes de fallback,
        # priorizando el sticky del host. Cuando un proxy de protocolo X falla,
        # se prueba uno de protocolo distinto antes que otro del mismo protocolo.
        last_exc: Exception | None = None
        attempted: set[str] = set()
        protocols_failed: set[str] = set()

        # Primer intento: el sticky del host (si existe y está sano)
        sticky = self.pool.get_for(self.target_host)
        if sticky is not None:
            attempted.add(sticky)
            try:
                r = self._execute(sticky, method, url, **kwargs)
                self.pool.report_success(sticky)
                return r
            except _PROXY_ERROR_TYPES as e:
                self.pool.report_failure(sticky)
                last_exc = e
                protocols_failed.add(_scheme_of(sticky))
                self.pool.clear_stickiness(self.target_host)
                log.info("proxy.attempt_failed", extra={
                    "proxy": _safe(sticky), "stage": "sticky", "error": str(e)[:120],
                })
            except Exception:
                self.pool.report_success(sticky)
                raise

        # Después: el resto del pool, alternando protocolos para no repetir fallos
        candidates = self.pool.healthy_proxies(exclude=attempted)
        ordered = _order_by_protocol_diversity(candidates, protocols_failed)
        for proxy in ordered[: max(1, self._max_attempts)]:
            attempted.add(proxy)
            try:
                r = self._execute(proxy, method, url, **kwargs)
                self.pool.report_success(proxy)
                return r
            except _PROXY_ERROR_TYPES as e:
                self.pool.report_failure(proxy)
                last_exc = e
                protocols_failed.add(_scheme_of(proxy))
                log.info("proxy.attempt_failed", extra={
                    "proxy": _safe(proxy), "protocol": _scheme_of(proxy),
                    "error": str(e)[:120],
                })
                continue
            except Exception:
                self.pool.report_success(proxy)
                raise

        # Último recurso: directo
        log.info("proxy.fallback_direct", extra={
            "target": self.target_host,
            "tried_count": len(attempted),
            "protocols_failed": sorted(protocols_failed),
        })
        try:
            return self._execute(None, method, url, **kwargs)
        except Exception as e:
            if last_exc is not None:
                raise e from last_exc
            raise

    def get(self, url: str, **kwargs) -> httpx.Response:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> httpx.Response:
        return self.request("POST", url, **kwargs)


# ---------------------------------------------------------------------------
# Singleton accessor
# ---------------------------------------------------------------------------

_POOL: ProxyPool | None = None
_POOL_LOCK = threading.Lock()


def get_pool() -> ProxyPool:
    global _POOL
    if _POOL is None:
        with _POOL_LOCK:
            if _POOL is None:
                _POOL = ProxyPool()
    return _POOL


def make_http_client(
    target_host: str,
    *,
    timeout: float = 60.0,
    headers: dict[str, str] | None = None,
) -> HttpClient:
    return HttpClient(target_host=target_host, pool=get_pool(), timeout=timeout, headers=headers)

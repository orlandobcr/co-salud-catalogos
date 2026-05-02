"""REPS scraper for prestadores.minsalud.gov.co/habilitacion.

The portal is an ASP.NET WebForms app behind a public guest login
(`invitado/invitado`). Each consultation page (sedes_reps.aspx,
serviciossedes_reps.aspx, ...) renders a DataGrid + an "Exportar a Texto"
image button (`_ctl0:ContentPlaceHolder1:ibText`) that dumps the FULL
filtered result set as a CSV-like file with `;` separator and ISO-8859-15
encoding.

Strategy:
1. POST work.aspx with `tbid_usuario=invitado&tbcontrasena=invitado`
   to obtain `ASP.NET_SessionId` cookie.
2. GET the consultation page → capture `__VIEWSTATE`,
   `__VIEWSTATEGENERATOR`, `__EVENTVALIDATION`.
3. POST a *minimal* body (only hidden tokens + `_ctl0:ibBuscarFtr.x/y`)
   to trigger the unfiltered search. Sending dropdown values back fails
   with "Invalid postback or callback argument" — Event Validation
   rejects values that weren't part of the original render.
4. POST again with `_ctl0:ContentPlaceHolder1:ibText.x/y` and
   `tbSeparator=;` → the response is the entire export (Content-Type
   `application/vnd.ms-notepad; charset=iso-8859-15`).

Empirically verified endpoints (May 2026):
- habilitados_reps.aspx           → 60,828 prestadores  (~21 MB)
- sedes_reps.aspx                  → 76,557 sedes        (~31 MB)
- serviciossedes_reps.aspx         → 228,207 servicios   (~157 MB)
- capacidadesinstaladas_reps.aspx  → 97,136 capacidades  (~33 MB)
"""

from __future__ import annotations

import csv
import io
import logging
import re
from typing import Any, Callable

from .proxy import HttpClient, make_http_client

log = logging.getLogger(__name__)

REPS_BASE = "https://prestadores.minsalud.gov.co"
REPS_HOST = "prestadores.minsalud.gov.co"
WORK_URL = f"{REPS_BASE}/habilitacion/work.aspx"
CONSULTAS_BASE = f"{REPS_BASE}/habilitacion/consultas/"

GUEST_USER = "invitado"
GUEST_PASS = "invitado"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) co-salud-catalogos/0.1"
)

CSV_SEPARATOR = ";"
EXPORT_ENCODING = "iso-8859-15"   # confirmed via Content-Type header
ROW_TERMINATOR = "\r"             # bare CR, classic Mac-style

ProgressCb = Callable[[int], None] | None


def _hidden(name: str, html: str) -> str:
    m = re.search(rf'name="{re.escape(name)}"[^>]*value="([^"]*)"', html)
    return m.group(1) if m else ""


def _state(html: str) -> dict[str, str]:
    return {
        "__VIEWSTATE": _hidden("__VIEWSTATE", html),
        "__VIEWSTATEGENERATOR": _hidden("__VIEWSTATEGENERATOR", html),
        "__EVENTVALIDATION": _hidden("__EVENTVALIDATION", html),
    }


def _client(*, use_proxy: bool = False) -> HttpClient:
    return make_http_client(
        REPS_HOST,
        timeout=600.0,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-CO,es;q=0.9",
        },
        use_proxy=use_proxy,
    )


def login(c: HttpClient) -> None:
    """POST guest credentials and populate session cookie on the client."""
    r = c.get(WORK_URL)
    r.raise_for_status()
    html = r.text
    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        **_state(html),
        "btn_eventos": "",
        "tbid_usuario": GUEST_USER,
        "tbcontrasena": GUEST_PASS,
        "Button1": "Ingresar",
    }
    r = c.post(WORK_URL, data=payload, headers={"Referer": WORK_URL})
    r.raise_for_status()
    if "ASP.NET_SessionId" not in c.cookies:
        raise RuntimeError("REPS login did not set ASP.NET_SessionId cookie")


def _search(c: HttpClient, url: str, html: str) -> str:
    """POST the unfiltered search; return new HTML with refreshed tokens."""
    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        **_state(html),
        "_ctl0:ibBuscarFtr.x": "37",
        "_ctl0:ibBuscarFtr.y": "14",
    }
    r = c.post(url, data=payload, headers={"Referer": url})
    r.raise_for_status()
    return r.text


def _export(c: HttpClient, url: str, html: str) -> bytes:
    """POST the ibText button; return the raw CSV bytes."""
    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        **_state(html),
        "_ctl0:ContentPlaceHolder1:tbSeparator": CSV_SEPARATOR,
        "_ctl0:ContentPlaceHolder1:ibText.x": "10",
        "_ctl0:ContentPlaceHolder1:ibText.y": "10",
    }
    r = c.post(url, data=payload, headers={"Referer": url})
    r.raise_for_status()
    return r.content


def _parse_csv(raw: bytes, *, progress_cb: ProgressCb = None) -> list[dict[str, Any]]:
    """Decode + parse the export. Handles bare CR line terminators."""
    text = raw.decode(EXPORT_ENCODING, errors="replace")
    # Normalize line endings so csv.DictReader works regardless of \r vs \r\n.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    buf = io.StringIO(text)
    reader = csv.DictReader(buf, delimiter=CSV_SEPARATOR)
    out: list[dict[str, Any]] = []
    for row in reader:
        # csv.DictReader leaves trailing None keys when a row has more cols than the header
        cleaned = {k: (v if v is not None else "") for k, v in row.items() if k}
        out.append(cleaned)
        if progress_cb is not None and len(out) % 5000 == 0:
            progress_cb(len(out))
    if progress_cb is not None:
        progress_cb(len(out))
    return out


def fetch_export(
    endpoint: str,
    *,
    progress_cb: ProgressCb = None,
    use_proxy: bool = False,
) -> list[dict[str, Any]]:
    """Fetch and parse a REPS consultation page export.

    `endpoint` is the page name, e.g. "sedes_reps.aspx" — the function
    prepends `CONSULTAS_BASE`.
    """
    url = endpoint if endpoint.startswith("http") else CONSULTAS_BASE + endpoint
    c = _client(use_proxy=use_proxy)
    login(c)
    r = c.get(url, headers={"Referer": WORK_URL})
    r.raise_for_status()
    html = r.text
    html = _search(c, url, html)
    raw = _export(c, url, html)
    return _parse_csv(raw, progress_cb=progress_cb)


def endpoint_url(endpoint: str) -> str:
    """Resolve a short endpoint name to the full URL (for metadata.source_url)."""
    return endpoint if endpoint.startswith("http") else CONSULTAS_BASE + endpoint

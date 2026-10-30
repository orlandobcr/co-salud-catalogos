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


# El export no escapa nada: un correo con varias direcciones separadas por `;`
# o un teléfono con un salto de línea adentro llegan tal cual y corren las
# columnas. Medido en habilitados_reps.aspx (29-oct-2026): 34 de 61.784 filas
# con separadores de más, casi todas en `email`, y 1 partida por un CRLF.
#
# Para repararlas se usan como anclas las columnas de formato fijo, reconocidas
# por el nombre del encabezado: si al absorber los campos sobrantes en una
# columna de texto libre todas las anclas validan, esa es la lectura correcta.
_SI_NO = re.compile(r"^(SI|NO)?$", re.IGNORECASE)
_DIGITS = re.compile(r"^\d*$")
_DATE8 = re.compile(r"^(\d{8})?$")
_CORTE = re.compile(r"^(Fecha corte.*)?$")

_DIGIT_COLUMNS = {
    "codigo_habilitacion", "nits_nit", "dv", "clpr_codigo", "naju_codigo",
    "numero_sede_principal", "sede_numero", "codigo_habilitacion_sede",
}

# Orden de preferencia para absorber separadores sobrantes cuando hay empate.
_FREE_TEXT_PREFERENCE = (
    "email", "telefono", "fax", "direccion", "gerente", "rep_legal",
    "nombre", "razon_social",
)

# Cuántas columnas distintas pueden tener separadores de más en una misma fila.
_MAX_MERGE_COLUMNS = 2

# Proporción de filas bien formadas en la que una regla tiene que cumplirse
# para usarla como ancla en ese export.
_ANCHOR_MIN_RATIO = 0.99


def _column_rule(name: str) -> re.Pattern | None:
    n = name.strip().lower()
    if n.startswith("fecha_corte"):
        return _CORTE
    if n.startswith("fecha_"):
        return _DATE8
    if n in {"habilitado", "ese"} or n.startswith("municipio"):
        return _SI_NO
    if n in _DIGIT_COLUMNS:
        return _DIGITS
    return None


def _preference(name: str) -> int:
    n = name.strip().lower()
    for i, prefix in enumerate(_FREE_TEXT_PREFERENCE):
        if n.startswith(prefix):
            return i
    return len(_FREE_TEXT_PREFERENCE)


def _split_records(text: str) -> list[str]:
    """Separa el export en registros.

    El terminador real es un CR suelto. Un LF (o CRLF) que aparezca es parte de
    un campo, así que se reemplaza por un espacio en vez de cortar la fila.
    Si algún día el export pasa a CRLF, se respeta.
    """
    cr = text.count("\r")
    crlf = text.count("\r\n")
    if cr and crlf < cr / 2:
        return text.replace("\r\n", " ").replace("\n", " ").split("\r")
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def _unquote(v: str) -> str:
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1].replace('""', '"')
    return v


def _violations(fields: list[str], rules: list[re.Pattern | None]) -> int:
    return sum(
        1 for v, rule in zip(fields, rules, strict=True) if rule is not None and not rule.match(v.strip())
    )


def _merge(tokens: list[str], plan: dict[int, int]) -> list[str]:
    """Une `plan[col]` tokens extra en la columna `col` (índices de columna)."""
    out: list[str] = []
    i = 0
    col = 0
    while i < len(tokens):
        extra = plan.get(col, 0)
        out.append(CSV_SEPARATOR.join(tokens[i : i + extra + 1]))
        i += extra + 1
        col += 1
    return out


def _repair(
    tokens: list[str],
    header: list[str],
    rules: list[re.Pattern | None],
) -> list[str] | None:
    """Reubica los separadores sobrantes de una fila larga.

    Prueba absorber los tokens extra en una columna de texto libre (o en dos)
    y se queda con la única lectura en la que todas las anclas validan. Entre
    varias lecturas válidas desempata por `_FREE_TEXT_PREFERENCE`; si aun así
    no hay una sola ganadora, la fila es irreparable.
    """
    extra = len(tokens) - len(header)
    free = [i for i, r in enumerate(rules) if r is None]
    plans: list[dict[int, int]] = [{c: extra} for c in free]
    if _MAX_MERGE_COLUMNS >= 2 and extra >= 2:
        for a_i, a in enumerate(free):
            for b in free[a_i + 1 :]:
                for k in range(1, extra):
                    plans.append({a: k, b: extra - k})

    valid: list[tuple[tuple[int, ...], list[str]]] = []
    for plan in plans:
        fields = _merge(tokens, plan)
        if len(fields) != len(header) or _violations(fields, rules):
            continue
        rank = tuple(sorted(_preference(header[c]) for c in plan))
        valid.append((rank, fields))
    if not valid:
        return None
    valid.sort(key=lambda t: t[0])
    if len(valid) > 1 and valid[0][0] == valid[1][0]:
        return None
    return valid[0][1]


def _calibrate(
    rules: list[re.Pattern | None], well_formed: list[list[str]]
) -> list[re.Pattern | None]:
    """Deja sólo las anclas que de verdad se cumplen en este export.

    Las reglas salen del nombre de la columna y cada endpoint del REPS usa sus
    propios formatos; una regla que falla en las filas bien formadas no sirve
    de ancla y haría descartar filas buenas. Se exige que valide en el
    `_ANCHOR_MIN_RATIO` de las filas con el número correcto de campos.
    """
    if not well_formed:
        # Sin filas de referencia no hay con qué calibrar: se usan tal cual.
        return rules
    calibrated: list[re.Pattern | None] = []
    for i, rule in enumerate(rules):
        if rule is None:
            calibrated.append(None)
            continue
        ok = sum(1 for f in well_formed if rule.match(f[i].strip()))
        calibrated.append(rule if ok >= _ANCHOR_MIN_RATIO * len(well_formed) else None)
    return calibrated


def parse_export(
    raw: bytes, *, progress_cb: ProgressCb = None
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Decodifica y parsea el export; devuelve `(filas, reporte)`.

    Las filas con el número correcto de campos se aceptan tal cual. Las largas
    se reparan con `_repair`; las cortas se completan si sólo les falta la
    cola. Las que no tienen arreglo se omiten y quedan en el reporte: meterlas
    con las columnas corridas rompe los tipos de la tabla (por ejemplo, un "NO"
    en `fecha_cierre`).
    """
    text = raw.decode(EXPORT_ENCODING, errors="replace")
    records = [r for r in _split_records(text) if r.strip()]
    report: dict[str, Any] = {"rows": 0, "repaired": 0, "padded": 0, "rejected": []}
    if not records:
        return [], report

    header = [h.strip() for h in records[0].split(CSV_SEPARATOR)]
    while header and header[-1] == "":
        header.pop()

    split: list[tuple[int, str, list[str]]] = []
    for line_no, rec in enumerate(records[1:], start=2):
        tokens = rec.split(CSV_SEPARATOR)
        # Las filas terminan en `;`: el último campo vacío no es una columna.
        if len(tokens) > len(header) and tokens[-1] == "":
            tokens.pop()
        split.append((line_no, rec, tokens))

    rules = _calibrate(
        [_column_rule(h) for h in header],
        [t for _, _, t in split if len(t) == len(header)],
    )

    out: list[dict[str, Any]] = []
    for line_no, rec, tokens in split:
        fields: list[str] | None = tokens
        if len(tokens) > len(header):
            fields = _repair(tokens, header, rules)
            if fields is not None:
                report["repaired"] += 1
        elif len(tokens) < len(header):
            # Fila corta: sólo se acepta si lo que falta es la cola y las anclas
            # presentes validan. Si no, viene truncada desde el origen.
            present = rules[: len(tokens)]
            if len(tokens) >= len(header) // 2 and not _violations(tokens, present):
                fields = tokens + [""] * (len(header) - len(tokens))
                report["padded"] += 1
            else:
                fields = None

        if fields is None:
            report["rejected"].append({"line": line_no, "fields": len(tokens), "head": rec[:80]})
            continue

        out.append({h: _unquote(v) for h, v in zip(header, fields, strict=True)})
        if progress_cb is not None and len(out) % 5000 == 0:
            progress_cb(len(out))

    report["rows"] = len(out)
    if progress_cb is not None:
        progress_cb(len(out))
    if report["repaired"] or report["padded"] or report["rejected"]:
        log.warning(
            "reps.parse_report repaired=%d padded=%d rejected=%d",
            report["repaired"], report["padded"], len(report["rejected"]),
        )
    return out, report


def _parse_csv(raw: bytes, *, progress_cb: ProgressCb = None) -> list[dict[str, Any]]:
    """Compatibilidad: sólo las filas de `parse_export`."""
    rows, _report = parse_export(raw, progress_cb=progress_cb)
    return rows


def fetch_export(
    endpoint: str,
    *,
    progress_cb: ProgressCb = None,
    use_proxy: bool = False,
    report: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Fetch and parse a REPS consultation page export.

    `endpoint` is the page name, e.g. "sedes_reps.aspx" — the function
    prepends `CONSULTAS_BASE`. If `report` is given, it is filled with the
    parse report (repaired / padded / rejected rows).
    """
    url = endpoint if endpoint.startswith("http") else CONSULTAS_BASE + endpoint
    c = _client(use_proxy=use_proxy)
    login(c)
    r = c.get(url, headers={"Referer": WORK_URL})
    r.raise_for_status()
    html = r.text
    html = _search(c, url, html)
    raw = _export(c, url, html)
    rows, parsed = parse_export(raw, progress_cb=progress_cb)
    if report is not None:
        report.update(parsed)
    return rows


def endpoint_url(endpoint: str) -> str:
    """Resolve a short endpoint name to the full URL (for metadata.source_url)."""
    return endpoint if endpoint.startswith("http") else CONSULTAS_BASE + endpoint

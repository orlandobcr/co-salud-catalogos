"""SISPRO ASPX scraper for MinSalud reference tables.

The page `https://web.sispro.gov.co/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx?Code=<X>`
returns an ASP.NET WebForms grid (`grvTablaReferencia`) populated server-side.

Strategy:
1. GET initial page → capture `__VIEWSTATE`, `__VIEWSTATEGENERATOR`, `__EVENTVALIDATION`,
   total item count (visible as "Pág. 1 Items NNNNN"), columns.
2. POST with `__EVENTTARGET=ctl00$cntContenido$dpggrvTablaReferencia$ddlPageSize`
   and `ddlPageSize=2000` to enlarge the grid.
3. POST `__EVENTTARGET=ctl00$cntContenido$grvTablaReferencia` +
   `__EVENTARGUMENT=Page$N` for each subsequent page.
4. Parse `<table id="ctl00_cntContenido_grvTablaReferencia">` from each
   response with lxml.

Empirically verified codes: CIE10 (12.6k), CUPS (10k), CodigoEAPByNit (1.7k),
IUM (34k).
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from typing import Any

from lxml import html as lxml_html

from .proxy import make_http_client

log = logging.getLogger(__name__)

SISPRO_BASE = "https://web.sispro.gov.co"
SISPRO_HOST = "web.sispro.gov.co"
SISPRO_PATH = "/WebPublico/Consultas/ConsultarDetalleReferenciaBasica.aspx"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Anonimiz/0.1 (Kashport)"
)

GRID_ID = "ctl00_cntContenido_grvTablaReferencia"
GRID_NAME = "ctl00$cntContenido$grvTablaReferencia"
PAGE_SIZE_NAME = "ctl00$cntContenido$dpggrvTablaReferencia$ddlPageSize"

DEFAULT_PAGE_SIZE = 2000


@dataclass
class PageState:
    viewstate: str
    viewstate_generator: str
    eventvalidation: str
    total_items: int | None
    columns: list[str]


def _build_url(code: str) -> str:
    return f"{SISPRO_BASE}{SISPRO_PATH}?Code={code}"


def _extract_state(tree) -> PageState:
    def _val(name: str) -> str:
        nodes = tree.xpath(f'//input[@name="{name}"]/@value')
        return nodes[0] if nodes else ""

    vs = _val("__VIEWSTATE")
    vsg = _val("__VIEWSTATEGENERATOR")
    ev = _val("__EVENTVALIDATION")

    # Total items label looks like "Pág. 1 Items NNNNN"
    total = None
    pg_text = " ".join(tree.xpath("//text()"))
    m = re.search(r"Items\s+(\d+)", pg_text)
    if m:
        total = int(m.group(1))

    cols: list[str] = []
    grid = tree.xpath(f'//table[@id="{GRID_ID}"]')
    if grid:
        header_row = grid[0].xpath('.//tr[1]/th')
        cols = [th.text_content().strip() for th in header_row]

    return PageState(
        viewstate=vs,
        viewstate_generator=vsg,
        eventvalidation=ev,
        total_items=total,
        columns=cols,
    )


def _parse_rows(tree, columns: list[str]) -> list[dict[str, Any]]:
    grid = tree.xpath(f'//table[@id="{GRID_ID}"]')
    if not grid:
        return []
    rows = grid[0].xpath('.//tr')
    out: list[dict[str, Any]] = []
    for tr in rows:
        # Skip rows that are header (only <th>) or pager
        ths = tr.xpath('./th')
        tds = tr.xpath('./td')
        if ths and not tds:
            continue
        if not tds:
            continue
        # Skip pager — it usually has only one <td> with colspan and links
        if len(tds) == 1 and tds[0].xpath('.//a[contains(@href, "Page$")]'):
            continue
        values = [td.text_content().strip() for td in tds]
        if columns and len(columns) == len(values):
            out.append(dict(zip(columns, values, strict=False)))
        else:
            # Fallback: positional dict
            out.append({f"col_{i}": v for i, v in enumerate(values)})
    return out


def _base_payload(state: PageState, code: str) -> dict[str, str]:
    return {
        "__VIEWSTATE": state.viewstate,
        "__VIEWSTATEGENERATOR": state.viewstate_generator,
        "__EVENTVALIDATION": state.eventvalidation,
        # Some hidden inputs the page expects:
        "VIEWPORT": "",
        "ctl00$cntContenido$TxtEmail": "",
    }


def fetch_all(
    code: str,
    *,
    page_size: int = DEFAULT_PAGE_SIZE,
    progress_cb=None,
    use_proxy: bool = True,
) -> tuple[list[dict[str, Any]], int | None]:
    """Fetch all rows of a SISPRO reference table by Code."""
    url = _build_url(code)
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-CO,es;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
    }

    c = make_http_client(SISPRO_HOST, timeout=120, headers=headers, use_proxy=use_proxy)
    # ---- Step 1: GET initial
    r = c.get(url)
    r.raise_for_status()
    tree = lxml_html.fromstring(r.content)
    state = _extract_state(tree)
    total = state.total_items

    # ---- Step 2: POST to set page size
    post_headers = {
        **headers,
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": SISPRO_BASE,
        "Referer": url,
    }
    payload_resize = {
        **_base_payload(state, code),
        "__EVENTTARGET": PAGE_SIZE_NAME,
        "__EVENTARGUMENT": "",
        PAGE_SIZE_NAME: str(page_size),
    }
    r = c.post(url, data=payload_resize, headers=post_headers)
    r.raise_for_status()
    tree = lxml_html.fromstring(r.content)
    state = _extract_state(tree)

    # ---- Step 3: parse first page rows
    rows = _parse_rows(tree, state.columns)
    if progress_cb is not None:
        progress_cb(len(rows))
    all_rows = list(rows)

    # ---- Step 4: paginate while there are more pages
    if total and len(all_rows) < total:
        page = 2
        max_pages = (total + page_size - 1) // page_size
        while page <= max_pages and len(all_rows) < total:
            payload_page = {
                **_base_payload(state, code),
                "__EVENTTARGET": GRID_NAME,
                "__EVENTARGUMENT": f"Page${page}",
                PAGE_SIZE_NAME: str(page_size),
            }
            r = c.post(url, data=payload_page, headers=post_headers)
            r.raise_for_status()
            tree = lxml_html.fromstring(r.content)
            state = _extract_state(tree)
            rows = _parse_rows(tree, state.columns)
            if not rows:
                log.warning("sispro.empty_page", extra={"code": code, "page": page})
                break
            all_rows.extend(rows)
            if progress_cb is not None:
                progress_cb(len(all_rows))
            page += 1

    return all_rows, total

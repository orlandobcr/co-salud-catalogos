"""Escritura a la base: cambio de tipos entre corridas y guarda de caída de filas."""

import os

import pytest
from sqlalchemy import inspect, text

from sync_catalogos.db import ShrinkGuardError, SqlSink
from sync_catalogos.schema import CatalogFile, CatalogMetadata


def catalog(entries, name="prueba"):
    meta = CatalogMetadata(
        name=name, description="", source="reps_export", source_url="", source_id=None,
        version="v", license="", row_count=len(entries), last_synced="2026-10-30T00:00:00+00:00",
        sha256="x" * 64, notes="",
    )
    return CatalogFile(metadata=meta, entries=entries)


# sqlite no aplica el límite de 63 caracteres de Postgres a los nombres, así
# que los tests corren también contra Postgres si hay uno disponible.
_PG_URL = os.environ.get("SALUD_TEST_PG_URL")


def _drop_all(s):
    with s.engine.begin() as c:
        for t in inspect(c).get_table_names():
            c.execute(text(f'DROP TABLE "{t}"'))


@pytest.fixture(params=["sqlite", "postgresql"])
def sink(request, tmp_path):
    if request.param == "sqlite":
        s = SqlSink(f"sqlite:///{tmp_path / 'salud.db'}")
    elif _PG_URL:
        s = SqlSink(_PG_URL)
        _drop_all(s)
    else:
        pytest.skip("SALUD_TEST_PG_URL no definido")
    s.ensure_schema()
    yield s
    if request.param == "postgresql":
        _drop_all(s)
    s.close()


def rows_of(sink, table="salud_prueba"):
    with sink.engine.connect() as c:
        return c.execute(text(f'SELECT * FROM "{table}" ORDER BY _idx')).mappings().all()


def test_columna_que_pasa_de_numero_a_texto(sink):
    # Primera corrida: sólo números → BIGINT.
    sink.write_catalog(catalog([{"codigo": "1", "fecha_cierre": "20240101"}] * 3))
    # Segunda corrida: aparece un texto. Antes fallaba el INSERT en Postgres
    # porque la tabla vieja no se alteraba.
    nuevos = [{"codigo": "1", "fecha_cierre": "20240101"}] * 2 + [{"codigo": "1", "fecha_cierre": "NO"}]
    sink.write_catalog(catalog(nuevos))
    rows = rows_of(sink)
    assert [r["fecha_cierre"] for r in rows] == ["20240101", "20240101", "NO"]


def test_tipo_se_decide_con_todas_las_filas(sink):
    # El texto aparece después de la fila 1000: con muestreo se anulaba en silencio.
    entries = [{"n": str(i)} for i in range(1500)] + [{"n": "N/A"}]
    sink.write_catalog(catalog(entries))
    rows = rows_of(sink)
    assert rows[-1]["n"] == "N/A"


def test_guarda_de_caida_conserva_lo_publicado(sink):
    sink.write_catalog(catalog([{"a": str(i)} for i in range(100)]))
    with pytest.raises(ShrinkGuardError):
        sink.write_catalog(catalog([{"a": "1"}] * 10))
    assert len(rows_of(sink)) == 100
    with sink.engine.connect() as c:
        assert c.execute(text("SELECT row_count FROM salud_catalog_metadata")).scalar() == 100


def test_descarga_vacia_no_borra_lo_publicado(sink):
    sink.write_catalog(catalog([{"a": "1"}] * 10))
    with pytest.raises(ShrinkGuardError):
        sink.write_catalog(catalog([]))
    assert len(rows_of(sink)) == 10


def test_allow_shrink(sink):
    sink.write_catalog(catalog([{"a": str(i)} for i in range(100)]))
    sink.max_shrink = None
    sink.write_catalog(catalog([{"a": "1"}] * 10))
    assert len(rows_of(sink)) == 10


def test_stream_y_normal_comparten_swap(sink):
    sink.write_catalog_stream(catalog([]).metadata, [[{"a": "1"}, {"a": "2"}], [{"a": "3"}]])
    assert [r["a"] for r in rows_of(sink)] == ["1", "2", "3"]
    sink.write_catalog(catalog([{"a": "x"}] * 3))
    assert [r["a"] for r in rows_of(sink)] == ["x", "x", "x"]


def test_nombre_largo_se_actualiza_dos_veces(sink):
    # El nombre de la tabla, el de staging y el de sus PK pasan de 63
    # caracteres. Antes el ALTER INDEX no encontraba la PK y abortaba el swap.
    nombre = "sispro_lce_responsables_envio_informacion_por_tipo_poblacion_especial"
    tabla = "salud_" + nombre
    for valor in ("x", "y"):
        sink.write_catalog_stream(catalog([], name=nombre).metadata, [[{"a": valor}]])
        sink.write_catalog(catalog([{"a": valor}], name=nombre))
    with sink.engine.connect() as c:
        guardada = c.execute(
            text("SELECT table_name FROM salud_catalog_metadata WHERE name = :n"), {"n": nombre}
        ).scalar_one()
    assert [r["a"] for r in rows_of(sink, guardada)] == ["y"]
    assert len(guardada) <= 63 and tabla.startswith(guardada)

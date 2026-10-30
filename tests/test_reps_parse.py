"""Parseo del export del REPS: filas con separadores de más, partidas o truncadas.

Los casos reproducen las formas reales vistas en habilitados_reps.aspx el
29-oct-2026, con datos inventados.
"""

from sync_catalogos.reps import EXPORT_ENCODING, parse_export

HEADER = (
    "depa_nombre;muni_nombre;codigo_habilitacion;nombre_prestador;tido_codigo;nits_nit;"
    "razon_social;clpr_codigo;clpr_nombre;ese;direccion;telefono;fax;email;gerente;nivel;"
    "caracter;habilitado;fecha_radicacion;fecha_vencimiento;fecha_cierre;dv;clase_persona;"
    "naju_codigo;naju_nombre;numero_sede_principal;fecha_corte_REPS;telefono_adicional;"
    "email_adicional;rep_legal;Municipio PDET;Municipio ZOMAC"
)


def row(email="contacto@ejemplo.co", telefono="3001234567", nombre="CLINICA EJEMPLO SAS"):
    return (
        f"Antioquia;MEDELLIN;0500100001;{nombre};;900000001;{nombre};1;"
        f"Instituciones Prestadoras de Servicios de Salud - IPS;NO;CALLE 1 # 2-3;{telefono};;"
        f"{email};;;;SI;20200101;20280101;;7;JURIDICO;1;Privada;01;"
        "Fecha corte REPS: Oct 29 2026  8:23PM;;;PEDRO PRUEBA;NO;SI;"
    )


def export(*rows: str, terminator: str = "\r") -> bytes:
    return terminator.join([HEADER, *rows, ""]).encode(EXPORT_ENCODING)


def test_filas_normales():
    rows, report = parse_export(export(row(), row()))
    assert len(rows) == 2
    assert rows[0]["email"] == "contacto@ejemplo.co"
    assert rows[0]["fecha_cierre"] == ""
    assert report["repaired"] == 0 and not report["rejected"]


def test_varios_correos_separados_por_punto_y_coma():
    rows, report = parse_export(export(row(email="a@ejemplo.co; b@ejemplo.co; c@ejemplo.co")))
    assert report["repaired"] == 1
    r = rows[0]
    assert r["email"] == "a@ejemplo.co; b@ejemplo.co; c@ejemplo.co"
    assert r["habilitado"] == "SI"
    assert r["fecha_cierre"] == ""
    assert r["Municipio ZOMAC"] == "SI"


def test_crlf_dentro_de_un_campo_no_parte_la_fila():
    rows, report = parse_export(export(row(telefono="6720000\r\n6720001")))
    assert len(rows) == 1
    assert rows[0]["telefono"] == "6720000 6720001"
    assert not report["rejected"]


def test_fila_truncada_desde_la_fuente_se_omite():
    truncada = row().split(";")[:12]
    rows, report = parse_export(export(row(), ";".join(truncada), row()))
    assert len(rows) == 2
    assert len(report["rejected"]) == 1
    assert report["rejected"][0]["line"] == 3


def test_comillas_literales_se_conservan():
    rows, _ = parse_export(export(row(nombre='E.S.E. HOSPITAL "SAN PRUEBA"')))
    assert rows[0]["nombre_prestador"] == 'E.S.E. HOSPITAL "SAN PRUEBA"'


def test_campo_entero_entre_comillas_se_desenvuelve():
    rows, _ = parse_export(export(row(nombre='"FUNDACION PRUEBA"')))
    assert rows[0]["nombre_prestador"] == "FUNDACION PRUEBA"


def test_export_con_crlf_como_terminador():
    rows, report = parse_export(export(row(), row(), terminator="\r\n"))
    assert len(rows) == 2 and not report["rejected"]


def test_fila_bien_formada_nunca_se_descarta_por_las_anclas():
    # Un valor raro en una columna ancla no basta para perder la fila.
    rara = row().replace(";SI;20200101;", ";PENDIENTE;20200101;")
    rows, report = parse_export(export(row(), rara))
    assert len(rows) == 2 and not report["rejected"]


def test_regla_que_no_aplica_al_export_se_desactiva():
    # Si en este endpoint `fecha_radicacion` viene con otro formato, deja de ser
    # ancla, y las filas largas se siguen reparando con las demás.
    otra = lambda **kw: row(**kw).replace(";20200101;", ";2020-01-01;")  # noqa: E731
    rows, report = parse_export(export(otra(), otra(), otra(email="a@x.co; b@x.co")))
    assert len(rows) == 3
    assert report["repaired"] == 1
    assert rows[2]["email"] == "a@x.co; b@x.co"

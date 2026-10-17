"""
Pruebas unitarias para la lógica del negocio de alumnos matriculados y pagos en caja.
"""
from src.database import DB_ALUMNOS, DB_PAGOS, reset_db
from src.main import PagoCreate, obtener_alumnos_matriculados, registrar_pago_caja


def test_obtener_alumnos_filtrado_directo():
    reset_db()
    res = obtener_alumnos_matriculados("comunicacion")
    assert res["total_encontrados"] == 2
    nombres = [a["nombre"] for a in res["alumnos"]]
    assert "Ana Pérez" in nombres
    assert "Carlos Gómez" in nombres


def test_obtener_alumnos_sin_coincidencias():
    reset_db()
    res = obtener_alumnos_matriculados("filosofia")
    assert res["total_encontrados"] == 0
    assert res["alumnos"] == []


def test_registrar_pago_unidad():
    reset_db()
    pago_dto = PagoCreate(alumno_id=2, monto=80.0, concepto="Constancia de notas")
    res = registrar_pago_caja(pago_dto)

    assert res["mensaje"] == "Pago registrado exitosamente en caja"
    assert res["data"]["pago_id"] == 1
    assert res["data"]["monto"] == 80.0
    assert len(DB_PAGOS) == 1

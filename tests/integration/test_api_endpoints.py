"""
Pruebas de integración de endpoints para el módulo Académico y Caja.
"""

def test_alumnos_matriculados_comunicacion(client):
    response = client.get("/api/v1/alumnos-matriculados", params={"curso": "comunicacion"})
    assert response.status_code == 200
    data = response.json()
    assert data["curso"] == "comunicacion"
    assert data["total_encontrados"] == 2
    assert len(data["alumnos"]) == 2
    assert data["alumnos"][0]["nombre"] == "Ana Pérez"
    assert data["alumnos"][1]["nombre"] == "Carlos Gómez"


def test_alumnos_matriculados_case_insensitive(client):
    # La búsqueda debe ser insensible a mayúsculas/minúsculas
    response = client.get("/api/v1/alumnos-matriculados", params={"curso": "COMUNICACION"})
    assert response.status_code == 200
    data = response.json()
    assert data["total_encontrados"] == 2


def test_alumnos_matriculados_matematica(client):
    response = client.get("/api/v1/alumnos-matriculados", params={"curso": "matematica"})
    assert response.status_code == 200
    data = response.json()
    assert data["total_encontrados"] == 1
    assert data["alumnos"][0]["id"] == 3
    assert data["alumnos"][0]["nombre"] == "Lucía Torres"


def test_alumnos_matriculados_curso_inexistente(client):
    response = client.get("/api/v1/alumnos-matriculados", params={"curso": "fisica_cuantica"})
    assert response.status_code == 200
    data = response.json()
    assert data["total_encontrados"] == 0
    assert data["alumnos"] == []


def test_alumnos_matriculados_parametro_faltante(client):
    # El parámetro 'curso' es obligatorio según el contrato
    response = client.get("/api/v1/alumnos-matriculados")
    assert response.status_code == 422


def test_registrar_pago_caja_exitoso(client):
    payload = {
        "alumno_id": 1,
        "monto": 150.50,
        "concepto": "Cuota 01"
    }
    response = client.post("/api/v1/caja/pagos", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["mensaje"] == "Pago registrado exitosamente en caja"
    assert data["data"]["pago_id"] == 1
    assert data["data"]["alumno_id"] == 1
    assert data["data"]["monto"] == 150.50
    assert data["data"]["concepto"] == "Cuota 01"
    assert data["data"]["estado"] == "registrado"


def test_registrar_multiples_pagos_incrementa_id(client):
    pago1 = {"alumno_id": 1, "monto": 100.0, "concepto": "Cuota 01"}
    pago2 = {"alumno_id": 2, "monto": 200.0, "concepto": "Cuota 01"}

    res1 = client.post("/api/v1/caja/pagos", json=pago1)
    res2 = client.post("/api/v1/caja/pagos", json=pago2)

    assert res1.status_code == 201
    assert res2.status_code == 201
    assert res1.json()["data"]["pago_id"] == 1
    assert res2.json()["data"]["pago_id"] == 2


def test_registrar_pago_caja_payload_invalido(client):
    # 'monto' debe ser un número float/int
    payload_invalido = {
        "alumno_id": 1,
        "monto": "no_es_un_monto",
        "concepto": "Error"
    }
    response = client.post("/api/v1/caja/pagos", json=payload_invalido)
    assert response.status_code == 422

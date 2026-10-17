@siga-u @spec-first
Feature: Módulos Académico y Caja
  Como usuario o sistema cliente
  Quiero consultar alumnos matriculados por curso y registrar pagos en caja
  Para mantener la gestión académica y financiera sincronizada

  Background:
    Given la base de datos en memoria está inicializada con los alumnos mock:
      | id | nombre        | curso        |
      | 1  | Ana Pérez     | comunicacion |
      | 2  | Carlos Gómez  | comunicacion |
      | 3  | Lucía Torres  | matematica   |
    And la base de datos de pagos está vacía

  Scenario: Consultar alumnos matriculados en curso con múltiples estudiantes
    When se realiza una petición GET a "/api/v1/alumnos-matriculados?curso=comunicacion"
    Then el código de respuesta debe ser 200
    And el campo "total_encontrados" debe ser 2
    And el campo "curso" debe ser "comunicacion"
    And la lista "alumnos" debe contener 2 registros
    And el primer alumno debe ser "Ana Pérez" con id 1
    And el segundo alumno debe ser "Carlos Gómez" con id 2

  Scenario: Consultar alumnos matriculados en curso con un solo estudiante
    When se realiza una petición GET a "/api/v1/alumnos-matriculados?curso=matematica"
    Then el código de respuesta debe ser 200
    And el campo "total_encontrados" debe ser 1
    And el campo "curso" debe ser "matematica"
    And el alumno debe tener id 3 y nombre "Lucía Torres"

  Scenario: Consultar alumnos de un curso sin estudiantes
    When se realiza una petición GET a "/api/v1/alumnos-matriculados?curso=historia"
    Then el código de respuesta debe ser 200
    And el campo "total_encontrados" debe ser 0
    And la lista "alumnos" debe estar vacía

  Scenario: Registrar un pago exitoso en caja
    When se realiza una petición POST a "/api/v1/caja/pagos" con el cuerpo:
      """json
      {
        "alumno_id": 1,
        "monto": 150.00,
        "concepto": "Matrícula Semestre 2026-I"
      }
      """
    Then el código de respuesta debe ser 201
    And el campo "mensaje" debe ser "Pago registrado exitosamente en caja"
    And el registro de pago en "data" debe contener:
      | campo     | valor                    |
      | pago_id   | 1                        |
      | alumno_id | 1                        |
      | monto     | 150.0                    |
      | concepto  | Matrícula Semestre 2026-I |
      | estado    | registrado               |

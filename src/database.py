"""
Simulación de ORM / Base de datos estática en memoria para SIGA-U Mini.
"""

DB_ALUMNOS = [
    {"id": 1, "nombre": "Ana Pérez", "curso": "comunicacion"},
    {"id": 2, "nombre": "Carlos Gómez", "curso": "comunicacion"},
    {"id": 3, "nombre": "Lucía Torres", "curso": "matematica"}
]

DB_PAGOS = []


def reset_db():
    """Restaura la base de datos en memoria a su estado inicial (útil para pruebas)."""
    global DB_ALUMNOS, DB_PAGOS
    DB_ALUMNOS.clear()
    DB_ALUMNOS.extend([
        {"id": 1, "nombre": "Ana Pérez", "curso": "comunicacion"},
        {"id": 2, "nombre": "Carlos Gómez", "curso": "comunicacion"},
        {"id": 3, "nombre": "Lucía Torres", "curso": "matematica"}
    ])
    DB_PAGOS.clear()

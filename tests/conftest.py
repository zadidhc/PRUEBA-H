import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.database import reset_db


@pytest.fixture(autouse=True)
def run_around_tests():
    """Reinicia la base de datos simulada antes de cada prueba para aislamiento total."""
    reset_db()
    yield
    reset_db()


@pytest.fixture
def client():
    """Cliente HTTP de prueba para interactuar con la app FastAPI."""
    return TestClient(app)

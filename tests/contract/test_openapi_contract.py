"""
Pruebas de contrato: validan que las rutas y métodos implementados en FastAPI
coincidan con la especificación formal en specs/03-api/openapi.yaml.
"""
from pathlib import Path
import yaml
from src.main import app


def test_rutas_coinciden_con_openapi_yaml():
    spec_path = Path("specs/03-api/openapi.yaml")
    assert spec_path.exists(), "La especificación specs/03-api/openapi.yaml debe existir."

    with open(spec_path, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    expected_paths = set(spec.get("paths", {}).keys())
    implemented_paths = {route.path for route in app.routes}

    # Todas las rutas esperadas en la spec deben estar implementadas
    for path in expected_paths:
        assert path in implemented_paths, f"Ruta esperada '{path}' no está implementada en FastAPI."


def test_metodos_http_coinciden_con_openapi_yaml():
    spec_path = Path("specs/03-api/openapi.yaml")
    with open(spec_path, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    route_map = {route.path: route.methods for route in app.routes}

    for path, methods_dict in spec.get("paths", {}).items():
        assert path in route_map
        for http_method in methods_dict.keys():
            assert http_method.upper() in route_map[path], (
                f"Método {http_method.upper()} para ruta '{path}' no implementado."
            )

import pytest
from fastapi.testclient import TestClient
from app import create_app


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    with TestClient(app) as client:
        yield client

from src.main import create_app
import os
import pytest


@pytest.fixture
def client():
    os.environ['FLASK_CONFIG_PATH'] = 'config/test.cfg'
    app = create_app()
    return app.test_client()


def test_health(client):
    response = client.get('/health')
    assert response.data.decode('utf-8').lower() == 'ok'
    assert response.status_code == 200

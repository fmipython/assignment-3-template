from src.main import create_app
import os
import pytest


@pytest.fixture
def client():
    os.environ['FLASK_CONFIG_PATH'] = 'config/base.cfg'
    app = create_app()
    return app.test_client()


def test_metrics_success(client):
    client.get('/metrics')
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['calls'] >= 1
    assert response.json['endpoints']['metrics']['calls'] >= 1
    assert response.json['endpoints']['metrics']['sent_bytes'] >= 1
    assert response.json['endpoints']['metrics']['errors'] == 0
    assert response.json['endpoints']['metrics']['response_codes']['200'] >= 1


def test_metrics_errors(client):
    client.get(
        '/non_existent_endpoint_nh945n45q9vn4v984nv-9b4-rv98b24rv0924btv20ub')
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['calls'] >= 1
    assert response.json['errors'] >= 1


def test_metrics_fail(client):
    client.get('/fail')
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['calls'] >= 1
    assert response.json['errors'] >= 1
    assert response.json['endpoints']['fail']['calls'] >= 1
    assert response.json['endpoints']['fail']['errors'] >= 1
    assert response.json['endpoints']['fail']['response_codes']['418'] >= 1


def test_reset_metrics(client):
    client.get('/metrics')
    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['calls'] >= 1
    assert response.json['sent_bytes'] >= 10
    last_clear = float(response.json['last_clear'])

    response = client.get('/reset_metrics')
    assert response.status_code == 200

    response = client.get('/metrics')
    assert response.status_code == 200
    assert response.json['calls'] == 1
    assert response.json['errors'] == 0
    assert float(response.json['last_clear']) > last_clear

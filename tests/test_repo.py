from src.main import create_app
import os
import pytest


@pytest.fixture
def client():
    os.environ['FLASK_CONFIG_PATH'] = 'config/base.cfg'
    app = create_app()
    return app.test_client()


def test_repo(client, token):
    response = client.get(
        '/repo/luchev/interview-prep-notes', headers={'token': token})
    assert response.status_code == 200
    assert response.json['result']['visibility'] == 'public'
    assert response.json['result']['name'] == 'interview-prep-notes'
    assert response.json['result']['html_url'] == 'https://github.com/luchev/interview-prep-notes'


def test_repo_error(client, token):
    response = client.get(
        '/repo/non_existent_user_nh945n45q9vn4v984nv-9b4-rv98b24rv0924btv20ub/repowhatever', headers={'token': token})
    assert response.status_code == 502

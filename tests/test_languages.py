from src.main import create_app
import os
import pytest


@pytest.fixture
def client():
    os.environ['FLASK_CONFIG_PATH'] = 'config/base.cfg'
    app = create_app()
    return app.test_client()


def test_languages(client, token):
    response = client.get(
        '/languages/luchev/interview-preparation', headers={'token': token})
    assert response.status_code == 200
    want_result = {
        "Python": 299435,
        "JavaScript": 114095,
        "C++": 66022,
        "Java": 65687,
        "Go": 24932, "TypeScript": 15421, "Rust": 1801, "Shell": 933, "Haskell": 220}
    for lang, lines in want_result.items():
        assert int(response.json['result'][lang]) >= lines


def test_languages_error(client, token):
    response = client.get(
        '/languages/non_existent_user_nh945n45q9vn4v984nv-9b4-rv98b24rv0924btv20ub/repowhatever', headers={'token': token})
    assert response.status_code == 502

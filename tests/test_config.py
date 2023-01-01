from src.main import create_app
import os


def test_config():
    os.environ['FLASK_CONFIG_PATH'] = 'config/test.cfg'
    app = create_app()
    client = app.test_client()

    response = client.get('/config')
    assert response.status_code == 200
    assert response.json['ENV'] == 'test'
    assert response.json['SECRET_KEY'] == ''

    os.environ['FLASK_CONFIG_PATH'] = 'config/production.cfg'
    app = create_app()
    client = app.test_client()

    response = client.get('/config')
    assert response.status_code == 200
    assert response.json['ENV'] == 'production'
    assert response.json['SECRET_KEY'] == ''

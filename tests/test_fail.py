from src.main import create_app
import os


def test_fail():
    os.environ['FLASK_CONFIG_PATH'] = 'config/test.cfg'
    app = create_app()
    client = app.test_client()

    response = client.get('/fail')
    assert response.status_code == 418

    os.environ['FLASK_CONFIG_PATH'] = 'config/production.cfg'
    app = create_app()
    client = app.test_client()

    response = client.get('/fail')
    assert response.status_code == 404

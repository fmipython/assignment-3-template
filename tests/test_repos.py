from src.main import create_app
import os
import pytest


@pytest.fixture
def client():
    os.environ['FLASK_CONFIG_PATH'] = 'config/base.cfg'
    app = create_app()
    return app.test_client()


def test_repos(client, token):
    response = client.get('/repos/luchev', headers={'token': token})
    assert response.status_code == 200
    want_result = {'BOLE',
                   'FMICodes2020',
                   'algorithms',
                   'article-recommendation-engine-svd',
                   'assembly-string-encryption',
                   'barry-voice-assistant',
                   'booky-server',
                   'cargo-junit',
                   'cargo-results',
                   'chrome-extension-calculator',
                   'chrome-extension-yet-another-lenny',
                   'course-nand-to-tetris',
                   'cpp-beautifier',
                   'customer-segmentation-report-arvato',
                   'data-structures-and-algorithms',
                   'disaster-response-pipeline',
                   'distributed-testing-framework-for-rust',
                   'dotfiles',
                   'google-playstore-data-analysis',
                   'hackerrank-scraper',
                   'interview-prep-notes',
                   'interview-preparation',
                   'markdown-editor',
                   'markdown-editor-demo-website',
                   'meteo-station-air-quality-visualizer',
                   'minify',
                   'most-popular-language-2020-stackoverflow',
                   'parallel-bfs',
                   'rush',
                   'self-driving-car',
                   'skandia-plugin-advanced-inventory-manager',
                   'skandia-plugin-daily-loyalties',
                   'skandia-plugin-xutilities',
                   'suffix-automaton',
                   'testing-framework',
                   'uni-data-structures-and-algorithms-2019',
                   'uni-object-oriented-programming-2019',
                   'uni-object-oriented-programming-2021',
                   'vscode-p2p-live-codeshare',
                   'wallpaperabyss-downloader',
                   'xml-generator-from-dtd',
                   'xml-parser'}

    assert want_result.issubset(set(response.json['result']))


def test_repos_error(client, token):
    response = client.get(
        '/repos/non_existent_user_nh945n45q9vn4v984nv-9b4-rv98b24rv0924btv20ub', headers={'token': token})
    assert response.status_code == 502

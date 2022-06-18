import pytest
import json
from app import create_app

app = create_app()


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_get_user(client):
    rv = client.get('/user')
    assert len(json.loads(rv.data.decode('utf-8'))['data'][0]) == 5
    return

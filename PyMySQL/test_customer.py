import pytest
from multiprocessing import Process
from app import create_app

app = create_app()


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def work(client, url):
    client.get(url)
    return


def test_get_customer_info(client):
    for i in range(100):
        work(client, '/customer/payment')
    return

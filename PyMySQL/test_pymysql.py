import pytest
from threading import Thread
from app import create_app

app = create_app()

global_queue = []


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def work(client, url):
    rv = client.get(url)
    global_queue.append(rv.status_code)
    return


def test_get_customer_info(client):
    t1 = Thread(target=work, args=[client, '/customer'])
    t1.start()
    t2 = Thread(target=work, args=[client, '/order'])
    t2.start()
    t3 = Thread(target=work, args=[client, '/customer/payment'])
    t3.start()
    t4 = Thread(target=work, args=[client, '/customer/order'])
    t4.start()
    t5 = Thread(target=work, args=[client, '/order/test'])
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    for status_code in global_queue :
        assert status_code == 200
    return None

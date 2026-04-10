import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_orders():
    res = requests.get(f"{BASE_URL}/posts")
    assert res.status_code == 200
    assert len(res.json()) > 0


def test_invalid_order():
    res = requests.get(f"{BASE_URL}/posts/9999")
    assert res.status_code == 404 or res.json() == {}
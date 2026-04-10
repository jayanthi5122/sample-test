import os
import pytest
import requests

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")


def _headers():
    return {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }


@pytest.mark.skipif(not API_KEY, reason="REQRES_API_KEY not set")
def test_get_user():
    res = requests.get(f"{BASE_URL}/users/2", headers=_headers())
    assert res.status_code == 200
    body = res.json()
    assert "data" in body
    assert body["data"]["id"] == 2


@pytest.mark.skipif(not API_KEY, reason="REQRES_API_KEY not set")
def test_create_user():
    payload = {
        "name": "kishore",
        "job": "tester"
    }

    res = requests.post(f"{BASE_URL}/users", json=payload, headers=_headers())
    assert res.status_code == 201
    body = res.json()
    assert body["name"] == "kishore"
    assert body["job"] == "tester"


@pytest.mark.skipif(not API_KEY, reason="REQRES_API_KEY not set")
def test_invalid_user():
    res = requests.get(f"{BASE_URL}/users/9999", headers=_headers())
    assert res.status_code == 404


def test_reqres_without_api_key_behavior():
    res = requests.get(f"{BASE_URL}/users/2")
    assert res.status_code in [200, 401, 403]
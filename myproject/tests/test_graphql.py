import requests

URL = "https://countries.trevorblades.com/"

def test_fetch_countries():
    query = {
        "query": "{ countries { code name } }"
    }

    res = requests.post(URL, json=query)

    assert res.status_code == 200
    assert "data" in res.json()


def test_invalid_query():
    query = {
        "query": "{ invalidField }"
    }

    res = requests.post(URL, json=query)

    assert res.status_code == 200
    assert "errors" in res.json()
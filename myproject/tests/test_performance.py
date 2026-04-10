import requests
import time

def test_api_response_time():
    start = time.time()

    res = requests.get("https://httpbin.org/delay/2")

    duration = time.time() - start

    assert res.status_code == 200
    assert duration < 5
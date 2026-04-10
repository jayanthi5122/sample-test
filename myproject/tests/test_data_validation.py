import pandas as pd

def test_detect_invalid_order_user_ids():
    users = pd.DataFrame([
        {"id": 1},
        {"id": 2}
    ])

    orders = pd.DataFrame([
        {"userId": 1},
        {"userId": 3}
    ])

    invalid = orders[~orders["userId"].isin(users["id"])]

    assert len(invalid) == 1
    assert invalid.iloc[0]["userId"] == 3
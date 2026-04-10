import json

def validate():
    with open("data/sample_users_orders.json") as f:
        data = json.load(f)

    users = {u["id"] for u in data["users"]}

    invalid_orders = [o for o in data["orders"] if o["userId"] not in users]

    return invalid_orders
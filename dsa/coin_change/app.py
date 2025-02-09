import math

from flask import Flask, request

app = Flask(__name__)


@app.post("/")
def get_order_packaging():
    request_body = request.json
    ignore_invalid_orders_in_response = request_body.get("ignore_invalid_orders_in_response", True)
    permissible_increments = request_body.get("permissible_increments", [0.5])
    number_of_available_bags = len(request_body["available_bag_sizes"])
    available_bag_sizes = sorted(request_body["available_bag_sizes"], reverse=True)

    invalid_orders = set()
    response = {"per_order": {}, "total": {}}
    for o in request_body["client_orders"]:
        order = o
        order_bags = {}
        for position, size in enumerate(available_bag_sizes, start=1):
            count = math.floor(order / size)
            order -= (size * count)
            if order != 0 and position == number_of_available_bags:
                if order in permissible_increments:
                    count += math.ceil(order)
                else:
                    invalid_orders.add(str(o))
                    order_bags.clear()
                    continue
            order_bags[str(size)] = count
            response["total"][str(size)] = response["total"].get(str(size), 0) + count
        if order_bags:
            response["per_order"][str(o)] = order_bags
    if not ignore_invalid_orders_in_response and invalid_orders:
        invalid_orders = list(invalid_orders)
        error_suffix = invalid_orders[-1]
        if len(invalid_orders) > 1:
            error_suffix = f'{", ".join(invalid_orders[:-1])} and {error_suffix}'
        return {"error": f"Incorrect order #{error_suffix}", "code": "bad_request"}, 400
    return response


if __name__ == '__main__':
    app.run()

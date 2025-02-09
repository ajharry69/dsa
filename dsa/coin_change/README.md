# Coin-change algorithm

An implementation of the [Change-making problem](https://en.wikipedia.org/wiki/Change-making_problem).

## Testing

The algorithm is implemented using flask web framework. Therefore, to test run the following:

1. `python3 -m venv .venv` - create a virtual environment.
2. `source .venv/bin/activate` - activate the virtual environment created above.
3. `pip install --upgrade-strategy=eager --upgrade pip` - upgrade the default `pip` package.
4. `pip install --upgrade-strategy=eager --upgrade flask` - install `flask` web framework.
5. `FLASK_APP=app.py flask run --debug` - start flask development server (with autoreload).

Send a `POST` request to the endpoint with the algorithm implementation:

```shell
curl -X POST --location 'http://127.0.0.1:5000' -H 'Content-Type: application/json' -d '{
  "ignore_invalid_orders_in_response": false,
  "permissible_increments": [0.5],
  "client_orders": [11, 5.5, 7, 7],
  "available_bag_sizes": [1, 2, 4]
}'
```
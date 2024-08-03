import flask
import json
import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

app = flask.Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n+1, 2):
        if n % i == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


@app.route("/")
def index():
    return json.dumps({
        "code": 0

    })


if __name__ == "__main__":
    # 服务器使用，必须在所有变量定义好之前
    process_pool = ProcessPoolExecutor()
    app.run()

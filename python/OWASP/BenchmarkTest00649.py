
import os
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-01/BenchmarkTest00649", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    param = request.args.get('BenchmarkTest00649', '')
    if param is None:
        param = ""

    bar = encode_for_html(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = bar
    return response


def encode_for_html(data):
    return data.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")


if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02046", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    param = ""

    referer_header = request.headers.get("Referer")
    if referer_header:
        param = referer_header

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

def do_something(request, param):
    bar = "safe!"
    map81510 = {
        "keyA-81510": "a-Value",
        "keyB-81510": param,
        "keyC": "another-Value"
    }
    bar = map81510["keyB-81510"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

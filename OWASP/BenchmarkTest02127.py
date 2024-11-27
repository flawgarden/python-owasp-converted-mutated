
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-04/BenchmarkTest02127", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02127", "")
    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    return response


def do_something(request, param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

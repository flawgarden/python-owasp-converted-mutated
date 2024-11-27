
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-04/BenchmarkTest02404", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)


def handle_request(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest02404", "")
    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response


def do_something(request, param):
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

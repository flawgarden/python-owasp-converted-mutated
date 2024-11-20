
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-04/BenchmarkTest02395", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.args.get('BenchmarkTest02395', '')

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = f"Formatted like: a and {bar}."

    return response


def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
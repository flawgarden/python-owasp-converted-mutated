
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02680", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02680", "")
    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.data = response.response_format(bar, *obj)
    
    return response

def do_something(param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

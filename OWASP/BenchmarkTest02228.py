
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02228", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.content_type = "text/html;charset=UTF-8"

    params = request.args if request.method == 'GET' else request.form
    param = ""
    if params:
        values = params.getlist('BenchmarkTest02228')
        if values:
            param = values[0]

    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

def do_something(param):
    sbxyz60124 = str(param)
    bar = sbxyz60124 + "_SafeStuff"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, Response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01585", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    values = request.values.getlist('BenchmarkTest01585')
    param = values[0] if values else ""

    bar = Test().do_something(param)

    response = Response()
    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    return response

class Test:

    def do_something(self, param):
        bar = html.escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

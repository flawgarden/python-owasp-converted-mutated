
from flask import Flask, request, Response
from werkzeug.utils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01342", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest01342', '')

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = f"Formatted like: a and {bar}."
    return response

class Test:
    def do_something(self, param):
        bar = escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

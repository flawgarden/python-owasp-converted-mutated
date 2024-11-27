
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01590", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    values = request.args.getlist("BenchmarkTest01590")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    return response

class Test:
    def do_something(self, param):
        return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')

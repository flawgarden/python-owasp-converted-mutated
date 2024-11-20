
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01592", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"
    values = request.values.getlist("BenchmarkTest01592")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    headers = {"X-XSS-Protection": "0"}
    return bar, response_content, headers

class Test:

    def do_something(self, param):
        bar = ""
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

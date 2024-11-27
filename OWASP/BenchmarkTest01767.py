
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01767", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = request.args.get("BenchmarkTest01767")

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

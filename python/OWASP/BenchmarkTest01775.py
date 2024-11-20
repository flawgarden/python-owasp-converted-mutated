
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01775", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest01775')

    result = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(result)
    return response

class Test:
    def do_something(self, param):
        bar = ""

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01428", methods=['GET', 'POST'])
def benchmark_test_01428():
    if request.method == 'GET':
        return benchmark_test_01428_post()
    return benchmark_test_01428_post()

def benchmark_test_01428_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    for name in request.args.keys():
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01428":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = bar.encode('utf-8')
    return response

class Test:
    def do_something(self, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

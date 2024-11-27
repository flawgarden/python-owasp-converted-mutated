
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01514", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest01514", "")

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)

    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map56316 = {}
        map56316["keyA-56316"] = "a_Value"
        map56316["keyB-56316"] = param
        map56316["keyC"] = "another_Value"
        bar = map56316["keyB-56316"]
        bar = map56316["keyA-56316"]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

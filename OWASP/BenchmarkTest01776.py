
import os
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01776", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest01776')

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar is not None:
        length = len(bar)
        response.data = bar[:length]

    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map3531 = {}
        map3531["keyA-3531"] = "a_Value"
        map3531["keyB-3531"] = param
        map3531["keyC"] = "another_Value"

        bar = map3531.get("keyB-3531")
        bar = map3531.get("keyA-3531")

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

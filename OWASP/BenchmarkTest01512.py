
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01512", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest01512", "")
    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = f"{bar % ('a', 'b')}".encode('utf-8')
    return response

class Test:
    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            sbxyz76583 = list(param)
            sbxyz76583[-1] = "Z"
            bar = ''.join(sbxyz76583)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

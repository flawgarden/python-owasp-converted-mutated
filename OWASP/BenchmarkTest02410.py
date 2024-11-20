
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02410", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02410", "")
    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    length = len(bar) if bar else 1
    response.set_data(bar[:length])
    return response

def do_something(request, param):
    sbxyz69687 = str(param)
    bar = sbxyz69687 + "_SafeStuff"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

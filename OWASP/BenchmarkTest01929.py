
import os
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01929", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest01929' in request.headers:
        param = request.headers['BenchmarkTest01929']

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    a1, a2 = ("cmd.exe", "/c") if os.name == 'nt' else ("sh", "-c")
    args = [a1, a2, "echo " + bar]

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - subprocess error")
        raise e

    return response

def do_something(request, param):
    bar = "safe!"
    map44 = {}
    map44["keyA-44"] = "a-Value"
    map44["keyB-44"] = param
    map44["keyC"] = "another-Value"
    bar = map44["keyB-44"]

    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

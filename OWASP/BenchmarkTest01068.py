
import os
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01068", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    param = request.headers.get("BenchmarkTest01068", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == "nt":  # Windows
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        result = os.popen(cmd + bar).read()
        response.set_data(result)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
        return response

    return response

class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

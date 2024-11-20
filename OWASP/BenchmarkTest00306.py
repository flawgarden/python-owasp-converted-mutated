
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/cmdi-00/BenchmarkTest00306", methods=['GET', 'POST'])
def benchmark_test_00306():
    if request.method == 'GET':
        return benchmark_test_00306_post()
    return benchmark_test_00306_post()

def benchmark_test_00306_post():
    response = Response(content_type="text/html;charset=UTF-8")
    param = ""

    if "BenchmarkTest00306" in request.headers:
        param = request.headers["BenchmarkTest00306"]

    param = urllib.parse.unquote(param)

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    cmd = os.getenv("COMMAND_EXECUTION_STRING", "")
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = urllib.parse.quote(str(e))

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')

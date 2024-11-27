
import os
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-02/BenchmarkTest01939", methods=['GET', 'POST'])
def benchmark_test_01939():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.headers.get("BenchmarkTest01939", '')

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    cmd = get_insecure_os_command_string()
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

    return response


def do_something(request, param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar


def get_insecure_os_command_string():
    return "your_command_here"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

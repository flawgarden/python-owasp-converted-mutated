
from flask import Flask, request, render_template
import os
import urllib.parse
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02067", methods=['GET', 'POST'])
def benchmark_test_02067():
    if request.method == 'GET':
        return benchmark_test_02067_post()

    return benchmark_test_02067_post()

def benchmark_test_02067_post():
    param = ""
    headers = request.headers.getlist("BenchmarkTest02067")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = []

    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "  # Modified command for demonstration
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        result = subprocess.run(args, env=args_env, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {str(e)}"

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

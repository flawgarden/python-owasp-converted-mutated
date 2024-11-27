
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        bar = param
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        return bar

@app.route("/cmdi-01/BenchmarkTest01687", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01687="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter 'BenchmarkTest01687' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(" ".join(args))
        result = process.read()
        return result
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {e}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

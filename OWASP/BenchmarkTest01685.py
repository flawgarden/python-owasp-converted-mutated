
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/cmdi-01/BenchmarkTest01685", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return "", 405  # Method not allowed

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01685="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter 'BenchmarkTest01685' in query string.", 400

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    bar = Test().do_something(request, param)

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
        cmd = f"ls {bar}"
        args = [a1, a2, cmd]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        return output, 200
    except Exception as e:
        return str(e), 500

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

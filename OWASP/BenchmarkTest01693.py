
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01693", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return "Method not allowed", 405

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01693="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string."

    param = query_string[param_loc + len(paramval):]  # Default to last parameter
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo"  # or some other command for Windows

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + " " + bar)
        output = process.read()
        return output  # Modify as necessary to return/handle command output
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {str(e)}"

class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01690", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01690="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval}' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()

    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        result = p.read()
        p.close()
        return result
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {str(e)}"

class Test:
    def do_something(self, request, param):
        bar = param
        return bar

def get_insecure_os_command_string():
    # Replace with the actual logic to retrieve the insecure OS command string
    return "echo"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

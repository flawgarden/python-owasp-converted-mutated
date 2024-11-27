
from flask import Flask, request, render_template
import subprocess
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01691", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01691="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01691' in query string."

    param = query_string[param_loc + len(paramval):]  # assume it's last parameter
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = Test().do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]

    try:
        result = subprocess.run([cmd] + args_env, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

def get_insecure_os_command_string():
    # Utility function to simulate getting insecure command string
    return "your_command_here"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

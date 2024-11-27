
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-03/BenchmarkTest02613", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02613="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02613' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param.replace("%20", " ")  # Simple URL decode for spaces

    bar = do_something(param)

    cmd = Utils.get_insecure_os_command_string()
    args_env = [bar]
    
    try:
        p = os.popen(cmd + ' ' + ' '.join(args_env))
        result = p.read()
        p.close()
        return result
    except Exception as e:
        return str(e)

def do_something(param):
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

class Utils:
    @staticmethod
    def get_insecure_os_command_string():
        return "your_command_here"  # Placeholder for actual command

if __name__ == "__main__":
    app.run(host='0.0.0.0')

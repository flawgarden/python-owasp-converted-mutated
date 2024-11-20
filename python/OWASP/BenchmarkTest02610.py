
from flask import Flask, request, Response
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-03/BenchmarkTest02610", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02610="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02610' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

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
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))
        results = process.read()
        process.close()
        return Response(results, mimetype='text/html')
    except Exception as e:
        return str(e)

def do_something(param):
    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

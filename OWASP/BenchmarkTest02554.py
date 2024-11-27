
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-03/BenchmarkTest02554", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02554="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02554' in query string."

    param = query_string[param_loc + len(paramval):]  # assume it's last
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    file_target = os.path.join("path/to/testfiles", bar)
    response_msg = f"Access to file: '{file_target}' created."
    
    if os.path.exists(file_target):
        response_msg += " And file already exists."
    else:
        response_msg += " But file doesn't exist yet."

    return response_msg

def do_something(param):
    bar = param
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

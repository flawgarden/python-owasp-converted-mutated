
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/pathtraver-03/BenchmarkTest02556", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02556="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02556' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    bar = do_something(param)

    file_target = bar
    response = f"Access to file: '{file_target}' created."
    
    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."
    
    return response


def do_something(param):
    num = 196
    return param if (500 / 42) + num > 200 else "This should never happen"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

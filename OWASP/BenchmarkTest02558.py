
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02558", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02558="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02558' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    file_target = os.path.join(bar, "Test.txt")
    response_text = f"Access to file: '{file_target}' created."

    if os.path.exists(file_target):
        response_text += " And file already exists."
    else:
        response_text += " But file doesn't exist yet."

    return response_text

def do_something(request, param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

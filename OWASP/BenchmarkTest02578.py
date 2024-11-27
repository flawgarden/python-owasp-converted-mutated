
import urllib.parse
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02578", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02578="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        response.set_data(f"getQueryString() couldn't find expected parameter 'BenchmarkTest02578' in query string.")
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.set_data(bar % tuple(obj))
    return response

def do_something(param):
    bar = "This should never happen" if (7 * 42) - 106 > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

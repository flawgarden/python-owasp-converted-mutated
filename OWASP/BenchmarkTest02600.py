
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02600", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    else:
        return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest02600="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.set_data("getQueryString() couldn't find expected parameter 'BenchmarkTest02600' in query string.")
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = os.path.splitext(param)[0]  # Simulating URL decoding

    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    if bar is not None:
        response.set_data(bar)
    return response

def do_something(request, param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

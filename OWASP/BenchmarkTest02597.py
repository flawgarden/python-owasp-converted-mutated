
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02597", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_response()

    return benchmark_test_response()

def benchmark_test_response():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02597="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02597' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        sbxyz19350 = list(param)
        sbxyz19350[-1] = 'Z'
        bar = ''.join(sbxyz19350)

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

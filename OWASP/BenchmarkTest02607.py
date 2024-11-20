
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02607", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02607="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02607' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    str_value = param if isinstance(param, str) else ""
    if str_value == "":
        str_value = "No cookie value supplied"

    response = make_response(f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: true")

    response.set_cookie('SomeCookie', str_value, secure=True, httponly=True, path=request.path)

    return response

def do_something(param):
    return f"{param}_SafeStuff"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
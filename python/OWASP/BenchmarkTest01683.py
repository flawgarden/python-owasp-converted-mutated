
import urllib.parse
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        # Mock of the ThingInterface and its method
        return param

@app.route("/securecookie-00/BenchmarkTest01683", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01683="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01683' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    str_value = param if isinstance(param, str) else ""
    if str_value == "":
        str_value = "No cookie value supplied"

    cookie = ("SomeCookie", str_value)
    response.set_cookie(cookie[0], cookie[1], secure=False, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: false"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

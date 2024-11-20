
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01684", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = make_response()
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01684="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01684' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    str_param = param if isinstance(param, str) else ""
    if str_param == "":
        str_param = "No cookie value supplied"
    
    cookie = ("SomeCookie", str_param)
    response.set_cookie(cookie[0], cookie[1], secure=True, httponly=True, path=request.path)

    response_data = f"Created cookie: 'SomeCookie': with value: '{html_encode(str_param)}' and secure flag set to: true"
    response.data = response_data
    return response

class Test:
    def do_something(self, request, param):
        sbxyz77558 = str(param)
        bar = sbxyz77558 + "_SafeStuff"
        return bar

def html_encode(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response, redirect
import base64
import os
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01675", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01675="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01675' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param  # No need to decode in this case; this is a simple example
    bar = Test().do_something(request, param)

    bytes_random = bytearray(random.getrandbits(8) for _ in range(10))
    remember_me_key = base64.b64encode(bytes_random).decode('utf-8')

    user = "Byron"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number
    found_user = False

    if cookie_name in request.cookies:
        if request.cookies[cookie_name] == request.cookies.get(cookie_name):
            found_user = True

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.path)
        request.environ['werkzeug.session'][cookie_name] = remember_me_key
        response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

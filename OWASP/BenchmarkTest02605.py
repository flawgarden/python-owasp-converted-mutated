
import os
from flask import Flask, request, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02605", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02605="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter 'BenchmarkTest02605' in query string.", 400

    param = query_string[param_loc + len(paramval):]  
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    value = random.random()
    remember_me_key = str(value)[2:]

    user = "Donna"
    full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie_name, cookie_value in cookies.items():
            if cookie_name == cookie_name and cookie_value == request.cookies.get(cookie_name):
                found_user = True

    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        remember_me = response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        request.session[cookie_name] = remember_me_key
        response.set_data(
            f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        )

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.random() executed")
    return response

def do_something(request, param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

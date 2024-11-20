
import os
import random
from flask import Flask, request, render_template, make_response, redirect, url_for
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02619", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02619="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02619' in query string."

    param = query_string[param_loc + len(paramval):]  # assumes param is last
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    rand = random.SystemRandom().random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "SafeFloyd"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if cookie_name == key:
                if value == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        response = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        return response

def do_something(param):
    bar = None
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

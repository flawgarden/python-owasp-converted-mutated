
import os
from flask import Flask, request, render_template, make_response, redirect
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01842", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-04/BenchmarkTest01842.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01842", "anything", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest01842", "anything", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if "BenchmarkTest01842" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest01842"])

        bar = do_something(request, param)
        value = random.random()
        remember_me_key = str(value)[2:]

        user = "Doug"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if cookie_name in the_cookies:
            if the_cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path, domain=request.host)
            request.environ['werkzeug.http.Session'].set(cookie_name, remember_me_key)
            return f"{user} has been remembered with cookie: {remember_me.name} whose value is: {remember_me.key}<br/>"

        return "Weak Randomness Test random.random() executed"

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

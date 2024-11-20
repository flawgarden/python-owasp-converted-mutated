
import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-03/BenchmarkTest01355", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest01355", "")
    bar = Test().do_something(param)

    rand = random.random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "Floyd"
    full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookie_name in cookies:
        if cookies[cookie_name] == request.cookies.get(cookie_name):
            found_user = True

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug.request'].session[cookie_name] = remember_me_key
        return remember_me

class Test:

    @staticmethod
    def do_something(param):
        from html import escape
        bar = escape(param)
        return bar


if __name__ == '__main__':
    app.run(host='0.0.0.0')

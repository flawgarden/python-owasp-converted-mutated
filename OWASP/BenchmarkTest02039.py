
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-04/BenchmarkTest02039", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    headers = request.headers.getlist("BenchmarkTest02039")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    value = random.random()
    remember_me_key = str(value)[2:]  # Trim off the 0. at the front.

    user = "Doug"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]  # Extract testCaseNumber
    user += test_case_number

    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True,
                                domain=request.host, path=request.path)
        request.environ['flask.session'][cookie_name] = remember_me_key
        response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.random() executed")
    return response


def do_something(param):
    bar = param  # In this case, encoding can be added as needed
    return bar


if __name__ == '__main__':
    app.run(host='0.0.0.0')

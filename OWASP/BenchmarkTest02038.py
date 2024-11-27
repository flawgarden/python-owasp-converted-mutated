
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02038", methods=['GET', 'POST'])
def benchmark_test_02038():
    if request.method == 'GET':
        return benchmark_test_02038_post()
    return benchmark_test_02038_post()

def benchmark_test_02038_post():
    response = make_response()
    param = ""
    headers = request.headers.get("BenchmarkTest02038")

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    value = random.random()
    remember_me_key = str(value)[2:]  # Trim off the 0. at the front.

    user = "Doug"
    full_class_name = type(app).__name__
    test_case_number = full_class_name[full_class_name.rfind('BenchmarkTest') + len('BenchmarkTest'):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie and cookies[cookie] == request.cookies.get(cookie_name):
                found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"

    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True,
                                domain=request.host, path=request.path)
        request.session[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.random() executed"
    return response

def do_something(request, param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
from flask import Flask, request, render_template, make_response, redirect, session, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Required for session management
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00560", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00560":
                    param = name
                    flag = False
                    break

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    value = random.random()
    rememberMeKey = str(value)[2:]  # Trim off the 0. at the front

    user = "Donna"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == session.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        response.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, domain=request.host)
        session[cookie_name] = rememberMeKey
        response.set_data(
            f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>"
        )

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.random() executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for session management
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00733", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.getlist('BenchmarkTest00733')
    param = param[0] if param else ""

    bar = param + "_SafeStuff"

    value = random.random()
    rememberMeKey = str(value)[2:]  # Trim off the 0. at the front.

    user = "Donna"
    full_class_name = __name__
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

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = response.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, domain=request.host, path=request.path)
        session[cookie_name] = rememberMeKey
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>"

    response.data += "Weak Randomness Test random.random() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

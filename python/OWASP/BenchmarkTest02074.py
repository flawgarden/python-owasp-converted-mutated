
import os
import random
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02074", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return render_template("index.html")

def benchmark_test_post():
    response = make_response()

    param = request.headers.get("BenchmarkTest02074", "")
    param = param # assuming it does not need URL decoding since we use Flask's request

    bar = do_something(param)

    rand = random.SystemRandom().random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "SafeDonna"
    test_case_number = "02074"  # Assuming a fixed case number for this test
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number
    found_user = False
    cookies = request.cookies

    if cookie_name in cookies:
        if cookies[cookie_name] == request.cookies.get(cookie_name):
            found_user = True

    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.SystemRandom().random() executed")
    return response

def do_something(param):
    return f"{param}_SafeStuff"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

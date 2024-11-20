
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00296", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    if "BenchmarkTest00296" in request.headers:
        param = request.headers.get("BenchmarkTest00296")

    param = param and param.encode().decode('utf-8')  # URL decode

    bar = "This should never happen" if (7 * 42) - 106 > 200 else param

    stuff = random.gauss(0, 1)
    remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

    user = "Gayle"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    if request.cookies:
        for cookie in request.cookies:
            if cookie_name == cookie:
                if request.cookies[cookie_name] == remember_me_key:
                    found_user = True

    response = make_response()
    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

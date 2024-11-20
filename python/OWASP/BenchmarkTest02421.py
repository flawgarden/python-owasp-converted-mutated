
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02421", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest02421", "")
    bar = do_something(param)

    stuff = random.gauss(0, 1)
    remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

    user = "Gayle"
    full_class_name = benchmark_test.__module__ + "." + benchmark_test.__qualname__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

def do_something(param):
    bar = "safe!"
    map85191 = {
        "keyA-85191": "a_Value",
        "keyB-85191": param,
        "keyC": "another_Value"
    }
    bar = map85191["keyB-85191"]
    bar = map85191["keyA-85191"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

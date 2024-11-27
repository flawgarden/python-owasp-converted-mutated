
import os
from flask import Flask, request, render_template, make_response, session
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # You should use a strong secret key in production.

@app.route("/weakrand-04/BenchmarkTest02139", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest02139", "")
    bar = do_something(param)

    rand = random.random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "Floyd"
    full_class_name = type(app).__name__
    test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie == cookie_name:
                if cookies[cookie] == session.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>".encode()
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.path)
        session[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode()

    response.data += b"Weak Randomness Test random.random() executed"
    return response


def do_something(param):
    bar = param  # In Python, we don't have built-in HTML escaping, so for this example, we'll just return the param.
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00461", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ''
    if request.args:
        param = request.args.get('BenchmarkTest00461', '')

    bar = param  # In a real case, you should use a proper escape function

    value = random.random()
    rememberMeKey = str(value)[2:]  # Trim off the 0. at the front.

    user = "Doug"
    full_class_name = 'BenchmarkTest00461'
    test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

    user += test_case_number
    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if cookie_name == key:
                if value == request.environ.get(cookie_name):
                    found_user = True
                    break

    response = make_response()
    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, domain=request.host.split(':')[0], path=request.path)
        request.environ[cookie_name] = rememberMeKey
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>"

    response.data += "Weak Randomness Test random.random() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

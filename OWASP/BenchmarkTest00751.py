
import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-01/BenchmarkTest00751", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    values = request.form.getlist("BenchmarkTest00751")
    param = values[0] if values else ""

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    try:
        rand = random.SystemRandom().random()

        remember_me_key = str(rand)[2:]  # Trim off the '0.' at the front.

        user = "SafeDonna"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for name, value in cookies.items():
                if cookie_name == name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"

        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: "
                             f"{cookie_name} whose value is: {remember_me_key}<br/>")
            request.cookies[cookie_name] = remember_me_key  # simulate session storing

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')

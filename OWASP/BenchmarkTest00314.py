
from flask import Flask, request, make_response, render_template
import urllib.parse
import os
import random
import secrets

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00314", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    param = request.headers.get("BenchmarkTest00314", "")

    param = urllib.parse.unquote(param)

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    try:
        rand = get_next_number()
        remember_me_key = str(rand)[2:]

        user = "SafeDonatella"
        full_class_name = "BenchmarkTest00314"
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
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
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response


def get_next_number():
    return secrets.randbelow(100) / 100


if __name__ == "__main__":
    app.run(host='0.0.0.0')

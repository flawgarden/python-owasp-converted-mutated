
import os
from flask import Flask, request, render_template, make_response
import random
import secrets

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-01/BenchmarkTest00667", methods=['GET', 'POST'])
def benchmark_test00667():
    if request.method == 'GET':
        return benchmark_test00667_post()
    return benchmark_test00667_post()


def benchmark_test00667_post():
    response = make_response()
    param = request.args.get("BenchmarkTest00667", "")

    bar = param if (7 * 42) - 106 <= 200 else "This should never happen"

    try:
        rand_number = secrets.randbelow(99)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = benchmark_test00667.__module__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_key, cookie_value in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_meCookie = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            remember_meCookie.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response = remember_meCookie
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)

        response.data += "Weak Randomness Test executed"
    except Exception as e:
        print("Problem executing SecureRandom.nextInt(int) - TestCase")
        raise e

    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
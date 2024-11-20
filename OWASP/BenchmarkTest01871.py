
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01871", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-04/BenchmarkTest01871.html"))
        user_cookie = make_response("Setting cookie")
        user_cookie.set_cookie("BenchmarkTest01871", "whatever", max_age=60 * 3, secure=True)
        response.set_cookie("BenchmarkTest01871", "whatever", max_age=60 * 3, secure=True)
        return response

    param = "noCookieValueSupplied"
    cookies = request.cookies
    if cookies:
        if "BenchmarkTest01871" in cookies:
            param = cookies["BenchmarkTest01871"]

    bar = do_something(param)

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        remember_me_key = str(r)

        user = "SafeIngrid"
        test_case_number = "01871"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response(
                f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            )
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
            return response

    except Exception as e:
        print("Problem executing SecureRandom.nextInt() - TestCase")
        raise

    return "Weak Randomness Test executed"

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + 'Z'
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

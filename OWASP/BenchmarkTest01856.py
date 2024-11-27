
import os
from flask import Flask, request, render_template, make_response
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01856", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-04/BenchmarkTest01856.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01856", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest01856", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if cookies:
            param_cookie = cookies.get("BenchmarkTest01856")
            if param_cookie:
                param = urllib.parse.unquote(param_cookie)

        bar = do_something(request, param)

        remember_me_key = str(random.randint(0, 2**63 - 1))
        user = "Logan"
        class_name = benchmark_test.__name__
        test_case_number = class_name[len("BenchmarkTest"):]

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie.name == cookie_name:
                    if cookie.value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return response

    return "Weak Randomness Test random.randint() executed"

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

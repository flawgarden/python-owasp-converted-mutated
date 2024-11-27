
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


class Test:

    @staticmethod
    def do_something(param):
        # Simple ? condition that assigns constant to bar on true condition
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar


@app.route("/weakrand-02/BenchmarkTest01195", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    if "BenchmarkTest01195" in request.headers:
        param = request.headers.get("BenchmarkTest01195")

    param = urllib.parse.unquote(param)
    bar = Test.do_something(param)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = __name__
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
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: "
                             f"{cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise

    response.data += "Weak Randomness Test random.SystemRandom().random() executed"
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

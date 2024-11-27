
import os
import urllib.parse
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01201", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    headers = request.headers.get('BenchmarkTest01201')

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        stuff = random.SystemRandom().gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "SafeGayle"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.environ.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextGaussian() - TestCase")
        raise e

    response.data += "Weak Randomness Test executed"
    return response

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

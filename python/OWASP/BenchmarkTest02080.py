
import os
import random
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02080", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    headers = request.headers.get("BenchmarkTest02080")
    if headers:
        param = headers.split(",")[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    try:
        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "SafeGayle"
        test_case_number = "BenchmarkTest02080"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie == cookie_name:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return response("Welcome back: " + user + "<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['session'][cookie_name] = remember_me_key
            return response(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
    except Exception as e:
        print("Problem executing random.gauss() - TestCase", e)
        return "Error occurred", 500

    return "Weak Randomness Test random.gauss() executed"

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

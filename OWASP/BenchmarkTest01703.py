
import os
import base64
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01703", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01703="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01703' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeFloyd"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return remember_me
    except Exception as e:
        print("Problem executing SecureRandom.nextFloat() - TestCase")
        raise

if __name__ == "__main__":
    app.run(host='0.0.0.0')

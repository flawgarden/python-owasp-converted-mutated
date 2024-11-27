
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00666", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest00666", "")

    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + "Z"

    try:
        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]

        user = "SafeGayle"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__qualname__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if request.cookies[cookie_name] == request.session.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing random.gauss() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

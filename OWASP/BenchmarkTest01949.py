
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01949", methods=['GET', 'POST'])
def benchmark_test_01949():
    if request.method == 'GET':
        return benchmark_test_01949_post()
    return benchmark_test_01949_post()

def benchmark_test_01949_post():
    response = make_response("")
    param = request.headers.get("BenchmarkTest01949", "")

    param = param

    bar = do_something(request, param)

    try:
        rand = random.SystemRandom().random()      # More secure way to generate randomness
        remember_me_key = str(rand)[2:]            # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = benchmark_test_01949.__name__
        test_case_number = full_class_name[len("benchmark_test_"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode()
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].set_cookie(cookie_name, remember_me_key)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode()

    except Exception as e:
        print("Problem executing random.SystemRandom().random() - TestCase")
        raise Exception(e)

    response.data += "Weak Randomness Test random.SystemRandom().random() executed".encode()
    return response

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

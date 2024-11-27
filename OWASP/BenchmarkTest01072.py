
import os
import base64
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01072", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.headers.get("BenchmarkTest01072", "")
    param = base64.b64decode(param).decode('utf-8')

    bar = Test().do_something(param)

    try:
        rand = get_next_number()

        remember_me_key = str(rand)[2:]

        user = "SafeDonatella"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key, cookie_value in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase", e)

    response.data += "Weak Randomness Test executed"
    return response

def get_next_number():
    return random.SystemRandom().random()

class Test:
    def do_something(self, param):
        if param:
            bar = base64.b64encode(base64.b64decode(param.encode())).decode()
        else:
            bar = ""
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

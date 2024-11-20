
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01612", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()

    values = request.values.getlist("BenchmarkTest01612")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    try:
        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]

        user = "SafeGayle"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing random.gauss() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

class Test:
    def do_something(self, param):
        bar = param  # Simulating HTML escape with no actual escape for simplicity
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

# Simulating the common headers for demonstration
common_headers = {'User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding'}

@app.route("/weakrand-02/BenchmarkTest01137", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    for name in request.headers:
        if name in common_headers:
            continue  # If standard header, move on to next one
        param = name  # Grabs the name of the first non-standard header as the parameter value
        break

    bar = Test().do_something(param)

    try:
        rand = random.Random().random()  # Simulating SecureRandom
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = "BenchmarkTest01137"
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
                        break

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me_cookie = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            remember_me_cookie.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key  # Simulate session storage
            return remember_me_cookie

    except Exception as e:
        print("Problem executing random() - TestCase")
        raise Exception(e)

    return "Weak Randomness Test executed"

class Test:
    def do_something(self, param):
        return param + "_SafeStuff"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

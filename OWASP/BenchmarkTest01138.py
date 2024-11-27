
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01138", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    for name in request.headers:
        if name in common_headers():
            continue

        param = name
        break

    bar = Test().do_something(param)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeFloyd"
        full_class_name = type(app).__name__
        test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

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
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {remember_me.name} whose value is: {remember_me.value}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextFloat() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

class Test:

    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1] + "Z"

        return bar

def common_headers():
    return ['Accept', 'Accept-Language', 'Content-Type', 'User-Agent', 'Host', 'Cookie', 'Connection', 'Upgrade-Insecure-Requests']

if __name__ == "__main__":
    app.run(host='0.0.0.0')

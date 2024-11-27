
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01131", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Content-Type', 'Host']:  # Add other standard headers here
            continue
            
        param = name
        break

    bar = Test().do_something(param)

    r = random.randint(0, 2147483647)
    rememberMeKey = str(r)

    user = "Ingrid"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies
    if cookies:
        if cookie_name in cookies:
            if cookies[cookie_name] == request.environ.get(cookie_name):
                found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>")
        remember_me.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, path=request.path)
        request.environ[cookie_name] = rememberMeKey
        response = remember_me

    response.data += "Weak Randomness Test random.randint() executed"
    return response

class Test:

    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

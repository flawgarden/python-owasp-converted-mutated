
import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02117", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = make_response()
        param = request.args.get("BenchmarkTest02117", "")
        bar = do_something(request, param)

        value = random.random()
        remember_me_key = str(value)[2:]  # Trim off the 0. at the front.

        user = "Doug"
        full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

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
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True,
                                    domain=request.host_url.split('//')[1].split('/')[0],
                                    path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        response.data += "Weak Randomness Test random.random() executed"
        return response

def do_something(request, param):
    bar = "safe!"
    map_12987 = {
        "keyA-12987": "a-Value",
        "keyB-12987": param,
        "keyC": "another-Value"
    }
    bar = map_12987["keyB-12987"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

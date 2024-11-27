
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01183", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    headers = request.headers.getlist("BenchmarkTest01183")

    if headers:
        param = headers[0]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    rand = random.random()
    remember_me_key = str(rand).split('.')[1]

    user = "Floyd"
    full_class_name = "BenchmarkTest01183"
    test_case_number = full_class_name.split("BenchmarkTest")[1]
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie].encode() == request.cookies.get(cookie_name).encode():
                    found_user = True
                    break

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.path)
        request.environ['werkzeug.session'][cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.random() executed"
    return response

class Test:

    def do_something(self, request, param):
        bar = None
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

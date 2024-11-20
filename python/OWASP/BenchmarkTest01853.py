
import os
import random
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01853", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("weakrand-04/BenchmarkTest01853.html"))
        user_cookie = make_response('whatever', 60 * 3)
        user_cookie.set_cookie('BenchmarkTest01853', 'whatever', max_age=60*3, secure=True, path=request.path, domain=request.host.split(":")[0])
        return resp

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01853' in the_cookies:
            param = the_cookies['BenchmarkTest01853']

        bar = do_something(param)

        bytes_key = os.urandom(10)
        remember_me_key = bytes_key.hex()

        user = "Byron"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1]  # Extract class name
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if cookie_name in the_cookies:
            if the_cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path, domain=request.host.split(":")[0])
            request.cookies[cookie_name] = remember_me_key
            return f"{user} has been remembered with cookie: {remember_me.name} whose value is: {remember_me.value}<br/>"

    return "Weak Randomness Test executed"

def do_something(param):
    num = 196
    if (500 / 42) + num > 200:
        return param
    return "This should never happen"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

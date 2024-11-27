
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01857", methods=['GET', 'POST'])
def benchmark_test_01857():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-04/BenchmarkTest01857.html"))
        user_cookie = make_response()
        user_cookie.set_cookie('BenchmarkTest01857', 'whatever', max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie('BenchmarkTest01857', 'whatever', max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest01857' in the_cookies:
            param = the_cookies['BenchmarkTest01857']

        bar = do_something(param)

        remember_me_key = str(os.urandom(8).hex())
        user = "Logan"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        cookies = request.cookies

        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return response

    return "Weak Randomness Test executed"

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

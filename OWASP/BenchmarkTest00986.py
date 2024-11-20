
from flask import Flask, request, render_template, make_response
import random
import base64
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00986", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("weakrand-02/BenchmarkTest00986.html"))
        user_cookie = make_response("whatever")
        user_cookie.set_cookie("BenchmarkTest00986", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if the_cookies:
            param = the_cookies.get("BenchmarkTest00986", param)

        bar = Test().do_something(request, param)

        rand = random.random()
        remember_me_key = str(rand)[2:]

        user = "SafeDonatella"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if the_cookies:
            if cookie_name in the_cookies:
                if the_cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response("Remembering user")
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['session'][cookie_name] = remember_me_key

            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    return "Weak Randomness Test random.random() executed"

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

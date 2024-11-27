
import os
import random
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00990", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-02/BenchmarkTest00990.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00990", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.headers.add('Set-Cookie', user_cookie.headers['Set-Cookie'])
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"

        if "BenchmarkTest00990" in the_cookies:
            param = unquote(the_cookies["BenchmarkTest00990"])

        bar = Test().do_something(request, param)

        try:
            r = random.SystemRandom().randint(0, 2**31 - 1)
            remember_me_key = str(r)

            user = "SafeIngrid"
            test_case_number = "00990"
            user += test_case_number
            cookie_name = "rememberMe" + test_case_number

            found_user = False
            if cookie_name in the_cookies:
                if the_cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

            if found_user:
                response_text = f"Welcome back: {user}<br/>"
            else:
                remember_me = make_response()
                remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                request.environ['werkzeug.session'].set(cookie_name, remember_me_key) 
                response_text = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

            return response_text + "Weak Randomness Test executed"

        except Exception as e:
            print("Problem executing SecureRandom.nextInt() - TestCase")
            raise

class Test:
    def do_something(self, request, param):
        return param  # simplistically returning param for the sake of example

if __name__ == "__main__":
    app.run(host='0.0.0.0')

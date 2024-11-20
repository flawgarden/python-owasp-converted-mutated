
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00973", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-02/BenchmarkTest00973.html"))
        user_cookie = ('BenchmarkTest00973', 'whatever', 60 * 3)  # Store cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest00973' in the_cookies:
            param = the_cookies['BenchmarkTest00973']

        bar = Test().do_something(request, param)
        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "Gayle"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if cookie_name in the_cookies:
            if the_cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = (cookie_name, remember_me_key)
            response = make_response(f"{user} has been remembered with cookie: {remember_me[0]} whose value is: {remember_me[1]}<br/>")
            response.set_cookie(remember_me[0], remember_me[1], secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            return response + "Weak Randomness Test random.gauss() executed"

class Test:
    def do_something(self, request, param):
        bar = param # Escape HTML if needed
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

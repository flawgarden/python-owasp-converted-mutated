
import os
from flask import Flask, request, render_template, make_response
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00976", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-02/BenchmarkTest00976.html"))
        user_cookie = ('BenchmarkTest00976', 'whatever', {'max_age': 60 * 3, 'secure': True})
        response.set_cookie(*user_cookie)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies

        if 'BenchmarkTest00976' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest00976'])

        bar = Test().do_something(request, param)

        remember_me_key = str(random.getrandbits(64))
        user = "Logan"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if cookie_name in cookies:
            if cookies[cookie_name] == request.environ.get('session').get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response()
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
            request.environ.get('session')[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            return response

    return "Invalid Request"

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

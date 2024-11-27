
from flask import Flask, request, render_template, make_response
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00975", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("weakrand-02/BenchmarkTest00975.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00975", "whatever", max_age=60 * 3, secure=True, path=request.full_path)
        resp.set_cookie("BenchmarkTest00975", "whatever", max_age=60 * 3, secure=True, path=request.full_path)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies

        if "BenchmarkTest00975" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest00975"])

        bar = Test().do_something(request, param)

        rand_number = random.randint(0, 98)
        remember_me_key = str(rand_number)

        user = "Inga"
        test_case_number = "00975"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return "Welcome back: " + user + "<br/>"
        else:
            response = make_response(user + " has been remembered with cookie: " +
                                     cookie_name + " whose value is: " +
                                     remember_me_key + "<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.full_path)
            return response

        return "Weak Randomness Test random.randint(0, 98) executed"

class Test:
    def do_something(self, request, param):
        num = 106
        bar = param if (7 * 42) - num <= 200 else "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

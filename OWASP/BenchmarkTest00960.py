
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-02/BenchmarkTest00960", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-02/BenchmarkTest00960.html"))
        user_cookie = ('BenchmarkTest00960', 'anything', 60 * 3, request.path,
                       urllib.parse.urlparse(request.url).netloc)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], path=user_cookie[3],
                            domain=user_cookie[4], secure=True)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if the_cookies:
            param = the_cookies.get("BenchmarkTest00960", param)

        bar = Test().do_something(request, param)

        value = random.random()
        remember_me_key = str(value)[2:]

        user = "Doug"
        test_case_number = "BenchmarkTest00960"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie and cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True
                    break

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, path=request.path,
                                    domain=urllib.parse.urlparse(request.url).netloc, secure=True, httponly=True)
            request.environ['werkzeug.session'][cookie_name] = remember_me_key
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        return "Weak Randomness Test executed"


class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map19964 = {
            "keyA-19964": "a_Value",
            "keyB-19964": param,
            "keyC": "another_Value"
        }
        bar = map19964["keyB-19964"]
        bar = map19964["keyA-19964"]

        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

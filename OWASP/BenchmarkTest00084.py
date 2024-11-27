
import os
import random
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00084", methods=['GET', 'POST'])
def benchmark_test_00084():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-00/BenchmarkTest00084.html"))
        user_cookie = make_response("whatever")
        user_cookie.set_cookie("BenchmarkTest00084", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest00084", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        if request.cookies:
            for the_cookie in request.cookies:
                if the_cookie == "BenchmarkTest00084":
                    param = unquote(request.cookies[the_cookie])
                    break

        thing = ThingFactory.create_thing()
        bar = thing.do_something(param)

        remember_me_key = str(random.randint(0, 2**31 - 1))
        user = "Ingrid"
        class_name = benchmark_test_00084.__name__
        test_case_number = class_name[class_name.rindex('BenchmarkTest') + len('BenchmarkTest'):]

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if request.cookies:
            for cookie in request.cookies:
                if cookie_name == cookie:
                    if request.cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response()
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        return "Weak Randomness Test random.randint() executed"

class ThingFactory:
    @staticmethod
    def create_thing():
        return Thing()

class Thing:
    def do_something(self, param):
        return f"Doing something with {param}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

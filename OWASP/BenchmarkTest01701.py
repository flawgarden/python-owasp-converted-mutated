
import os
import urllib.parse
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01701", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01701="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01701' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    rand = random.SystemRandom().random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "SafeDonna"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

    user += test_case_number
    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.cookies[cookie_name] = remember_me_key  # Simulate session attribute
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.SystemRandom().random() executed"
    return response

class Test:
    def do_something(self, param):
        thing = self.create_thing()
        bar = thing.do_something(param)
        return bar

    def create_thing(self):
        return ThingInterface()

class ThingInterface:
    def do_something(self, param):
        return f"Processed: {param}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

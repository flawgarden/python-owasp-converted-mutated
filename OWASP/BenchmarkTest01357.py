
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01357", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    map = request.form.to_dict()
    param = ""

    if map:
        values = map.get("BenchmarkTest01357")
        if values:
            param = values[0]

    bar = Test().do_something(param)

    r = random.randint(0, 2147483647)
    remember_me_key = str(r)

    user = "Ingrid"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['wsgi.session'][cookie_name] = remember_me_key
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.randint() executed")
    return response

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

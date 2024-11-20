
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01788", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest01788")

    bar = Test().do_something(request, param)

    l = os.urandom(8)  # Generate a random key (not as weak as Random)
    remember_me_key = str(int.from_bytes(l, 'big'))

    user = "Logan"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        if cookie_name in cookies:
            if cookies[cookie_name] == request.session.get(cookie_name):
                found_user = True

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.session[cookie_name] = remember_me_key
        response.set_cookie(cookie_name, remember_me_key)
        return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    return "Weak Randomness Test os.urandom() executed"

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

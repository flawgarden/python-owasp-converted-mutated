
import os
import base64
import random
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02163", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02163', "")
    bar = do_something(param)

    try:
        l = random.SystemRandom().getrandbits(64)
        remember_me_key = str(l)

        user = "SafeLogan"
        full_class_name = "BenchmarkTest02163"
        test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for name, value in cookies.items():
                if cookie_name == name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = request.cookies.set(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            return f"{user} has been remembered with cookie: {remember_me.name} whose value is: {remember_me.value}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextLong() - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

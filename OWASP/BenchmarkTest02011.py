
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02011", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection', 'Upgrade-Insecure-Requests']: 
            continue  # If standard header, move on to next one
        
        param = name  # Grabs the name of the first non-standard header as the parameter
        break

    bar = do_something(param)

    try:
        rand = random.SystemRandom().random()

        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key, cookie_value in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"

        remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        return remember_me

    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        raise

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

def do_something(param):
    sbxyz64726 = str(param)
    bar = sbxyz64726 + "_SafeStuff"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

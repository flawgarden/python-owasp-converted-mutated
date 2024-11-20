
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00581", methods=['GET', 'POST'])
def benchmark_test_00581():
    if request.method == 'GET':
        return benchmark_test_00581_post()
    return benchmark_test_00581_post()

def benchmark_test_00581_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00581":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = escape_html(param)

    rand = random.Random().random()  # Using Python's random for simplicity

    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "SafeDonna"
    full_class_name = benchmark_test_00581.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

    response = make_response()
    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.Random().random() executed"
    return response

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import base64
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00580", methods=['GET', 'POST'])
def benchmark_test():
    param = ""
    flag = True
    for name in request.args.keys():
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00580":
                    param = name
                    flag = False

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        test_case_number = "00580"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie_name] == remember_me_key:
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            resp = make_response(
                f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            )
            resp.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return resp

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        return str(e), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

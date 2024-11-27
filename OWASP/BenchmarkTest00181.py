
import os
import random
from flask import Flask, request, render_template, make_response, escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00181", methods=['GET', 'POST'])
def benchmark_test():
    param = request.headers.get("BenchmarkTest00181", "")
    param = escape(param)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = 'BenchmarkTest00181'  # Simulates this class name
        test_case_number = full_class_name[full_class_name.index("Test"):]  # Extracts "Test00181"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False
        cookies = request.cookies

        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return response

    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        raise e

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

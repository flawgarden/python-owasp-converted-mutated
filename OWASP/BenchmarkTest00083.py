
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00083", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-00/BenchmarkTest00083.html"))
        user_cookie = make_response("whatever")
        user_cookie.set_cookie("BenchmarkTest00083", "whatever", max_age=180, secure=True, path=request.path, domain=request.host)
        response = user_cookie
        return response

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00083" in cookies:
            param = cookies.get("BenchmarkTest00083")

        bar = param if (500 / 42) + 196 > 200 else "This should never happen"
        rand_number = random.randint(0, 98)
        remember_me_key = str(rand_number)
        user = "Inga"
        test_case_number = "BenchmarkTest00083"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies is not None:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return response

        return "Weak Randomness Test random.randint(0, 98) executed"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

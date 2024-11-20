
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00082", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-00/BenchmarkTest00082.html"))
        user_cookie = ("BenchmarkTest00082", "whatever")
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies

        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == "BenchmarkTest00082":
                    param = cookie_value
                    break
        
        bar = f"{param}_SafeStuff"
        rand_number = random.randint(0, 98)
        remember_me_key = str(rand_number)

        user = "Inga"
        test_case_number = "BenchmarkTest00082"[-2:]
        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        if cookies:
            for cookie_name in cookies:
                if cookie_name == f"rememberMe{test_case_number}":
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response()
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            return_response = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            return_response += "Weak Randomness Test random.randint executed"
            return return_response

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00095", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("weakrand-00/BenchmarkTest00095.html"))
        user_cookie = make_response('whatever')
        user_cookie.set_cookie("BenchmarkTest00095", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        resp.headers.add('Set-Cookie', user_cookie.headers['Set-Cookie'])
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if "BenchmarkTest00095" in cookies:
            param = cookies["BenchmarkTest00095"]

        bar = "safe!"
        map45268 = {
            "keyA-45268": "a-Value",
            "keyB-45268": param,
            "keyC": "another-Value"
        }
        bar = map45268["keyB-45268"]

        try:
            stuff = random.gauss(0, 1)
            remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

            user = "SafeGayle"
            test_case_number = "00095"
            user += test_case_number

            cookie_name = f"rememberMe{test_case_number}"

            found_user = False
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

            if found_user:
                return f"Welcome back: {user}<br/>"
            else:
                response = make_response(
                    f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
                )
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                return response
        except Exception as e:
            print("Problem executing SecureRandom.nextGaussian() - TestCase")
            raise e

    return "Weak Randomness Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

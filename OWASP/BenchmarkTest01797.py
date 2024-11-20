
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01797", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = request.args.get("BenchmarkTest01797", "")
    bar = Test().do_something(param)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        test_case_number = "01797"
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
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        raise e

    response.data += "Weak Randomness Test executed"
    return response

class Test:

    def do_something(self, param):
        bar = "safe!"
        map85341 = {
            "keyA-85341": "a_Value",
            "keyB-85341": param,
            "keyC": "another_Value"
        }
        bar = map85341.get("keyB-85341")
        bar = map85341.get("keyA-85341")

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

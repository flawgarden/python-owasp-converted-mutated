
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02441", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    param = request.values.get("BenchmarkTest02441", "")
    bar = do_something(request, param)

    try:
        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "SafeGayle"
        test_case_number = "02441"
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
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextGaussian() - TestCase")
        return str(e)

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

def do_something(request, param):
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
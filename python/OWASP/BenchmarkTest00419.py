
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00419", methods=['GET', 'POST'])
def benchmark_test():
    param = request.args.get("BenchmarkTest00419", "")
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    try:
        stuff = random.uniform(0, 1)  # Simulating SecureRandom.nextGaussian()
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front

        user = "SafeGayle"
        test_case_number = "00419"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        response = make_response()
        if found_user:
            response.set_data("Welcome back: " + user + "<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")

        response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
        return response

    except Exception as e:
        print("Problem executing SecureRandom simulation - TestCase")
        raise

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00899", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = make_response()
        param = request.args.get("BenchmarkTest00899")
        bar = None
        guess = "ABC"
        switch_target = guess[1]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        value = str(double_random())  # Simulate the random double generation
        remember_me_key = value[2:]  # Trim off the 0. at the front.

        user = "Donna"
        class_name = "BenchmarkTest00899"  # Simulating this value as the class name
        test_case_number = class_name.replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: {cookie_name} "
                             f"whose value is: {remember_me_key}<br/>")
            request.cookies[cookie_name] = remember_me_key

        response.data += "Weak Randomness Test executed"

        return response

def double_random():
    import random
    return random.random()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

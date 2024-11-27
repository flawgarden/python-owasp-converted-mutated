
import os
import random
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01196", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""

    headers = request.headers.get("BenchmarkTest01196")
    if headers:
        param = headers

    param = param  # URL decode is not needed in Flask for headers

    bar = Test().do_something(param)

    try:
        num_gen = random.SystemRandom()  # Uses a secure random number generator
        rand = get_next_number(num_gen)

        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonatella"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response += f"Welcome back: {user}<br/>"
        else:
            response += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            response += f"We'll set cookie now<br/>"

            response += f"We'll remember the user with: {cookie_name} and value: {remember_me_key}<br/>"

            # Normally you'd set cookies here, but for the purpose of this function:
            # response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)

    except Exception as e:
        response += "Problem executing SecureRandom.nextDouble() - TestCase<br/>"
        response += str(e)

    response += "Weak Randomness Test executed"
    return response

def get_next_number(generator):
    return generator.random()

class Test:

    def do_something(self, param):
        bar = param  # In Flask, we don't need to HTML escape manually; it is handled in rendering
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00421", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get("BenchmarkTest00421", "")
    bar = param

    try:
        rand_number = random.SystemRandom().randint(0, 98)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key, cookie_value in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = f"{cookie_name}={remember_me_key}; Secure; HttpOnly; Path={request.path}"
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextInt(int) - TestCase")
        raise

    response.data += "Weak Randomness Test random.SystemRandom().randint(int) executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

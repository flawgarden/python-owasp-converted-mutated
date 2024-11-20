
import os
import random
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02444", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = jsonify()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02444", "")
    bar = do_something(request, param)

    try:
        rand_number = random.SystemRandom().randint(0, 98)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if key == cookie_name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode()
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode()

    except Exception as e:
        print("Problem executing SecureRandom.randint - TestCase")
        raise e

    response.data += b"Weak Randomness Test executed"
    return response

def do_something(request, param):
    bar = ""

    # Simple condition that assigns param to bar on false condition
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

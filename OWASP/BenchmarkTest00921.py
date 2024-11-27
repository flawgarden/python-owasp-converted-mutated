
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00921", methods=['GET', 'POST'])
def benchmark_test_00921():
    if request.method == 'GET':
        return benchmark_test_00921_post()
    return benchmark_test_00921_post()

def benchmark_test_00921_post():
    response = make_response()
    param = request.args.get("BenchmarkTest00921")

    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    try:
        rand_number = random.randint(0, 98)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = benchmark_test_00921.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response.data += f"Welcome back: {user}<br/>".encode()
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
            response.data += (f"{user} has been remembered with cookie: {cookie_name} whose value is: "
                              f"{remember_me_key}<br/>").encode()

    except Exception as e:
        print("Problem executing SecureRandom.nextInt(int) - TestCase")
        raise

    response.data += "Weak Randomness Test executed".encode()
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

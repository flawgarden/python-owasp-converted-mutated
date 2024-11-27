
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-01/BenchmarkTest00422", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest00422", "")
    
    bar = param
    num = 106
    if (7 * 42) - num > 200:
        bar = "This should never happen"

    try:
        r = random.SystemRandom().randint(0, 2**31 - 1)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1]
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
            response.data = f"Welcome back: {user}<br/>".encode()
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: "
                             f"{cookie_name} whose value is: {remember_me_key}<br/>").encode()

    except Exception as e:
        print("Problem executing SecureRandom.randint() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.SystemRandom().randint() executed".encode()
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')

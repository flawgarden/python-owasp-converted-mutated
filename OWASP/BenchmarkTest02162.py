
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/weakrand-05/BenchmarkTest02162", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02162", "")
    bar = do_something(param)

    try:
        r = random.SystemRandom().randint(0, 2**31 - 1)
        remember_me_key = str(r)

        user = "SafeIngrid"
        test_case_number = "02162"
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if request.cookies[cookie_name] == request.environ.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextInt() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.SystemRandom().randint() executed"
    return response

def do_something(param):
    from html import escape
    bar = escape(param)
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

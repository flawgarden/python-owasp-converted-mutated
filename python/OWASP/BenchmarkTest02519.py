
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02519", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    values = request.values.getlist("BenchmarkTest02519")
    param = values[0] if values else ""

    bar = do_something(param)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand).split(".")[1]  # Trim off the 0. at the front.

        user = "SafeDonna"
        test_case_number = "02519"
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie].encode() == request.cookies.get(cookie_name).encode():
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise

    response.data += "Weak Randomness Test random.SystemRandom().random() executed"
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + "Z"  # Replace last character with 'Z'
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

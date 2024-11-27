
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00319", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if 'BenchmarkTest00319' in request.headers:
        param = request.headers['BenchmarkTest00319']

    param = base64.urlsafe_b64decode(param).decode('utf-8')

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key in cookies:
                if cookie_name == cookie_key:
                    if cookies[cookie_key] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data += f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode('utf-8')

    except Exception as e:
        print("Problem executing SecureRandom.randint() - TestCase")
        raise

    response.data += "Weak Randomness Test random.SystemRandom.randint() executed".encode('utf-8')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

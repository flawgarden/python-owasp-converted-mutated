
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00750", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    values = request.form.getlist('BenchmarkTest00750')
    param = values[0] if values else ""

    bar = param
    if param and len(param) > 1:
        sbxyz18731 = list(param)
        sbxyz18731[-1] = 'Z'
        bar = ''.join(sbxyz18731)

    try:
        rand = random.SystemRandom().random()
        rememberMeKey = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies.get(cookie_name)
        if cookies:
            if cookies == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>"
        
    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        raise e

    response.data += "Weak Randomness Test executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

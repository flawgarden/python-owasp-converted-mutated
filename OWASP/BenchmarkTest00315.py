
import os
import random
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00315", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest00315' in request.headers:
        param = request.headers['BenchmarkTest00315']

    param = param

    bar = "safe!"
    map38775 = {
        "keyA-38775": "a_Value",
        "keyB-38775": param,
        "keyC": "another_Value"
    }
    bar = map38775["keyB-38775"]
    bar = map38775["keyA-38775"]

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "00315"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if 'cookies' in request.cookies:
            for cookie in request.cookies:
                if cookie_name == cookie:
                    if request.cookies[cookie].encode() == request.cookies[cookie_name]:
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e
    finally:
        response.data += "Randomness Test os.urandom executed"
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

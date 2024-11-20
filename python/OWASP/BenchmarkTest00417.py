
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00417", methods=['GET', 'POST'])
def benchmark_test00417():
    if request.method == 'GET':
        return benchmark_test00417_post()

    return benchmark_test00417_post()

def benchmark_test00417_post():
    response = make_response("")
    param = request.args.get("BenchmarkTest00417", "")
    
    bar = "This_should_always_happen" if (7 * 18) + 106 > 200 else param

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = type(benchmark_test00417).__module__ + "." + type(benchmark_test00417).__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if request.cookies[cookie_name] == request.session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data += f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode('utf-8')
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise
    
    response.data += "Randomness Test os.urandom executed".encode('utf-8')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

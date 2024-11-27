
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00416", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest00416', "")
    bar = "safe!"
    map22488 = {
        "keyA-22488": "a-Value",
        "keyB-22488": param,
        "keyC": "another-Value"
    }
    bar = map22488["keyB-22488"]

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie.name == cookie_name:
                    if cookie.value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['beaker.session'][cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {remember_me.name} whose value is: {remember_me.value}<br/>"
        
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e
    finally:
        response.data += "Randomness Test os.urandom() executed"
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

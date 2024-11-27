
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00413", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest00413", "")
    
    bar = "safe!"
    map27963 = {
        "keyA-27963": "a-Value",
        "keyB-27963": param,
        "keyC": "another-Value"
    }
    bar = map27963["keyB-27963"]

    try:
        random_bytes = random.getrandbits(40 * 8).to_bytes(40, 'big')
        remember_me_key = ''.join(
            [string.ascii_letters[random.randint(0, len(string.ascii_letters) - 1)] for _ in range(40)]
        )
        
        user = "SafeByron"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True
        
        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode()
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode()
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise

    response.data += b"Randomness Test random.getrandbits executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

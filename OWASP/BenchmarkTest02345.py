
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02345", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02345":
                    param = name
                    flag = False

    bar = do_something(param)

    try:
        random_bytes = bytearray(40)
        random.getrandbits(40 * 8)

        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    finally:
        response.data += "Randomness Test executed"

    return response

def do_something(param):
    bar = "safe!"
    map60514 = {
        "keyA-60514": "a-Value",
        "keyB-60514": param,
        "keyC": "another-Value"
    }
    bar = map60514.get("keyB-60514")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

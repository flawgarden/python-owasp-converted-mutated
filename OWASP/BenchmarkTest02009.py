
import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02009", methods=['GET', 'POST'])
def benchmark_test_02009():
    if request.method == 'GET':
        return benchmark_test_02009_post()
    return benchmark_test_02009_post()

def benchmark_test_02009_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    for name in request.headers:
        if name in common_headers():
            continue
        param = name
        break

    bar = do_something(request, param)

    try:
        random_bytes = bytearray(random.getrandbits(8) for _ in range(40))

        remember_me_key = encode_for_base64(random_bytes)

        user = "SafeBystander"
        full_class_name = benchmark_test_02009.__module__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.environ.get('session').get(cookie_name):
                    found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ.get('session')[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing random generation - TestCase")
        raise Exception(e)
    finally:
        response.data += "Randomness Test executed"

    return response

def do_something(request, param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def common_headers():
    return ['Host', 'User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding']

if __name__ == '__main__':
    app.run(host='0.0.0.0')

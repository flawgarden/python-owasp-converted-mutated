
import os
import urllib.parse
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-04/BenchmarkTest02076", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)


def benchmark_test_post(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest02076' in request.headers:
        param = request.headers['BenchmarkTest02076']

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    rand = get_next_number()

    remember_me_key = str(rand)[2:]

    user = "SafeDonatella"
    full_class_name = benchmark_test.__qualname__
    test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')
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
        response.data += f"Welcome back: {user}<br/>".encode()
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.session[cookie_name] = remember_me_key
        response.data += (f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>").encode()

    response.data += "Weak Randomness Test executed".encode()
    return response


def get_next_number():
    return random.SystemRandom().random()


def do_something(request, param):
    bar = "safe!"
    map_data = {
        "keyA-15760": "a-Value",
        "keyB-15760": param,
        "keyC": "another-Value"
    }
    bar = map_data.get("keyB-15760", bar)
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01910", methods=['GET', 'POST'])
def benchmark_test_01910():
    if request.method == 'GET':
        return benchmark_test_01910_post()
    elif request.method == 'POST':
        return benchmark_test_01910_post()


def benchmark_test_01910_post():
    response = make_response()
    param = request.headers.get("BenchmarkTest01910", "")
    param = os.getenv("QUERY_STRING")  # Simulating URL decoding

    bar = do_something(param)

    value = os.urandom(4)  # Simulated random value
    remember_me_key = str(int.from_bytes(value, 'big')).lstrip('0.')

    user = "Doug"
    full_class_name = type(benchmark_test_01910).__name__
    test_case_number = full_class_name.replace("BenchmarkTest", "")

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test executed"
    return response


def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

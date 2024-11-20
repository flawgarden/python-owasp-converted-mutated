
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01119", methods=['GET', 'POST'])
def benchmark_test_01119():
    if request.method == 'GET':
        return benchmark_test_01119_post()

    return benchmark_test_01119_post()

def benchmark_test_01119_post():
    response = make_response()
    param = ""
    names = request.headers

    for name in names:
        if name in common_headers:
            continue

        param = name
        break

    bar = Test().do_something(request, param)

    value = os.urandom(8)  # Simulating weak randomness
    remember_me_key = str(int.from_bytes(value, 'big')).zfill(16)

    user = "Doug"
    full_class_name = benchmark_test_01119.__qualname__
    test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie].value == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.full_path)
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.full_path)
        request.cookies[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test executed"
    return response

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in 'CD':
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

common_headers = {"Host", "User-Agent", "Accept", "Accept-Language", "Accept-Encoding", "Connection"}  # Example common headers

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02003", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    for name in request.headers:
        if name not in common_headers:
            param = name
            break

    bar = do_something(param)

    remember_me_key = str(random.randint(0, 2**31 - 1))
    user = "Ingrid"
    test_case_number = "02003"
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number
    found_user = False

    for cookie in request.cookies:
        if cookie_name == cookie:
            if request.cookies[cookie_name] == request.environ.get(cookie_name, None):
                found_user = True

    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ[cookie_name] = remember_me_key
        response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.randint() executed")
    return response

def do_something(param):
    a69278 = param
    b69278 = a69278 + " SafeStuff"
    b69278 = b69278[:-1] + "Chars"
    map69278 = {"key69278": b69278}
    c69278 = map69278["key69278"]
    d69278 = c69278[:-1]
    e69278 = base64.b64decode(base64.b64encode(d69278.encode())).decode()
    f69278 = e69278.split(" ")[0]

    # Placeholder for ThingInterface logic
    g69278 = "barbarians_at_the_gate"
    bar = g69278  # Example static return (replace with actual logic if necessary)

    return bar

common_headers = ["Accept", "User-Agent", "Content-Type", "Authorization"]

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
import base64
from flask import Flask, request, render_template, make_response, session
from urllib.parse import urlparse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)

@app.route("/weakrand-01/BenchmarkTest00898", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get("BenchmarkTest00898", None)

    bar = b""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode()))

    bytes = os.urandom(10)
    rememberMeKey = base64.b64encode(bytes).decode('utf-8')

    user = "Byron"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie, value in cookies.items():
            if cookie_name == cookie:
                if value == session.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>".encode()
    else:
        remember_me_cookie = make_response()
        remember_me_cookie.set_cookie(cookie_name, rememberMeKey, httponly=True, secure=True, path=request.path)
        session[cookie_name] = rememberMeKey
        response.data = (f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>").encode()

    response.data += b"Weak Randomness Test os.urandom() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

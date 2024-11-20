
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02000", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    for name in request.headers:
        if name in ["Content-Type", "User-Agent", "Accept", "Accept-Encoding", "Connection"]:
            continue

        param = name
        break

    bar = do_something(request, param)

    bytes = random.randbytes(10)
    remember_me_key = base64.b64encode(bytes).decode('utf-8')

    user = "Byron"
    full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == user:
                    found_user = True
                    break

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)

    response.data += "Weak Randomness Test executed"
    return response

def do_something(request, param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')

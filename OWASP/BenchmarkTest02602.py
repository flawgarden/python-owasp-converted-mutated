
import os
import base64
import random
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02602", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02602="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter 'BenchmarkTest02602' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = unquote(param)

    bar = do_something(param)

    remember_me_key = base64.b64encode(random.randbytes(10)).decode()

    user = "Byron"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

    user += test_case_number
    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookie == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data += f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test executed"
    return response

def do_something(param):
    a3617 = param
    b3617 = f"{a3617} SafeStuff"
    b3617 = b3617[:-1] + "Chars"
    map3617 = {'key3617': b3617}
    c3617 = map3617["key3617"]
    d3617 = c3617[:-1]
    e3617 = base64.b64decode(base64.b64encode(d3617.encode())).decode()
    f3617 = e3617.split(" ")[0]

    # Simulation of reflection-based operation
    bar = f"Processed value: {f3617}"  # Placeholder for actual reflection logic
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

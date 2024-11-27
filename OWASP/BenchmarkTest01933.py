
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01933", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.headers.get("BenchmarkTest01933", "")
    param = param.encode('utf-8').decode('utf-8')  # URL Decode the header value

    bar = do_something(param)

    remember_me_key = str(random.getrandbits(64))

    user = "Logan"
    class_name = type(request).__name__
    test_case_number = class_name[class_name.index("BenchmarkTest") + len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.cookies[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.getrandbits(64) executed"
    return response

def do_something(param):
    bar = ""
    if param:
        bar = param.split(" ")[0]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

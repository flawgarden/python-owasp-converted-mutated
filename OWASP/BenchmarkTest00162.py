
import random
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00162", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("BenchmarkTest00162"):
        param = request.headers.get("BenchmarkTest00162")

    param = urllib.parse.unquote(param)

    bar = param  # Note: HTML escaping is omitted in this example

    stuff = random.gauss(0, 1)
    remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front

    user = "Gayle"
    full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if cookie_name == key:
                if value == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.data += f"Welcome back: {user}<br/>".encode()
    else:
        response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
        response.data += (f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>").encode()

    response.data += "Weak Randomness Test random.gauss() executed".encode()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')

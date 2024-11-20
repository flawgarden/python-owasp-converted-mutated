
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02700", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = make_response()

    param = request.args.get("BenchmarkTest02700", None)

    bar = do_something(param)

    bytes_ = os.urandom(10)
    remember_me_key = bytes_.hex()

    user = "Byron"
    full_class_name = "BenchmarkTest02700"
    test_case_number = full_class_name[len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookie_name in cookies:
        if cookies[cookie_name] == request.cookies.get(cookie_name):
            found_user = True

    if found_user:
        response.data = "Welcome back: " + user + "<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        request.session[cookie_name] = remember_me_key
        response.data = (user + " has been remembered with cookie: "
                         + cookie_name + " whose value is: " + remember_me_key + "<br/>")

    response.data += "Weak Randomness Test os.urandom() executed"
    return response

def do_something(param):
    bar = ""
    if param is not None:
        bar = param.encode('utf-8').decode('base64').encode('utf-8').decode('utf-8')
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

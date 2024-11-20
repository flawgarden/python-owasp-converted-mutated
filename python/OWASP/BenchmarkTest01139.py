
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01139", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    for name in request.headers:
        if name in common_headers(): 
            continue

        param = name
        break

    bar = Test().do_something(param)

    try:
        stuff = random.Random().gauss(0, 1)
        remember_me_key = str(stuff).split('.')[1]  

        user = "SafeGayle"
        test_case_number = "01139"
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
            remember_me = response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing random.gauss() - TestCase")
        raise Exception(e)

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

class Test:

    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            bar = bar[:-1] + "Z"
        return bar

def common_headers():
    return set(['Content-Type', 'User-Agent', 'Accept', 'Host', 'Connection'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')

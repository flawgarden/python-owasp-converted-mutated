
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02499", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    values = request.values.getlist("BenchmarkTest02499")
    param = values[0] if values else ""

    bar = do_something(param)

    rand = random.random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

    user = "Floyd"
    full_class_name = type(request).__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie_name_key in cookies:
            if cookie_name_key == cookie_name:
                if cookies[cookie_name_key] == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.path)
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.random() executed"
    return response

def do_something(param):
    bar = ""
    if param:
        bar = param.encode('utf-8').decode('utf-8')  # mimic base64 encoding/decoding
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

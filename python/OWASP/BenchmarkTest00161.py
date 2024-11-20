
import os
import random
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00161", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response("")
    param = request.headers.get("BenchmarkTest00161", "")
    param = urllib.parse.unquote(param)

    bar = "safe!"
    map_91760 = {
        "keyA-91760": "a_Value",
        "keyB-91760": param,
        "keyC": "another_Value"
    }
    bar = map_91760.get("keyB-91760")
    bar = map_91760.get("keyA-91760")

    value = random.random()
    remember_me_key = str(value).split('.')[1]

    user = "Donna"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie_key in cookies:
            if cookie_name == cookie_key:
                if cookies[cookie_key] == request.environ.get('beaker.session').get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host, path=request.path)
        request.environ.get('beaker.session')[cookie_name] = remember_me_key
        response = remember_me

    response.data += "Weak Randomness Test random.random() executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

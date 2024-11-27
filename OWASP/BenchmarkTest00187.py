
import os
import base64
import random
import hashlib
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00187", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.headers.get("BenchmarkTest00187", "")
    param = base64.b64decode(param).decode('utf-8') if param else ""

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    try:
        r = random.SystemRandom().randint(0, 2**31 - 1)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"
        found_user = False

        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie == cookie_name:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['beaker.session'][cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextInt() - TestCase")
        raise Exception(e)

    response.data += "Weak Randomness Test random.SystemRandom().randint() executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

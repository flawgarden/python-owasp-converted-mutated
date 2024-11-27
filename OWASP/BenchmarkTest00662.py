
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, param_name):
        return self.request.args.get(param_name)


@app.route("/weakrand-01/BenchmarkTest00662", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00662")
    if param is None:
        param = ""

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.
        
        user = "SafeDonna"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode()
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: {cookie_name} "
                             f"whose value is: {remember_me_key}<br/>").encode()
        
    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        response.status_code = 500
        response.data = str(e).encode()

    response.data += b"Weak Randomness Test executed"
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

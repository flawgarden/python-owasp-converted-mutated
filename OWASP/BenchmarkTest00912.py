
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name, '')


@app.route("/weakrand-02/BenchmarkTest00912", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00912")

    bar = None
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_data(
                f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            )
            request.environ['beaker.session'][cookie_name] = remember_me_key

    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e

    response.set_data(response.get_data(as_text=True) +
                      "Randomness Test executed")
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

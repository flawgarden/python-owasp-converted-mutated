
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    @staticmethod
    def doSomething(param):
        bar = "alsosafe"
        if param:
            valuesList = ["safe", param, "moresafe"]
            valuesList.pop(0)  # remove the 1st safe value
            bar = valuesList[1]  # get the last 'safe' value
        return bar

@app.route("/weakrand-03/BenchmarkTest01358", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = make_response()
    param = request.args.get("BenchmarkTest01358", "")

    bar = Test.doSomething(param)

    r = random.randint(0, 2147483647)
    rememberMeKey = str(r)

    user = "Ingrid"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie_name in cookies:
            if cookie_name == cookie_name:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        return response.body("Welcome back: " + user + "<br/>")
    else:
        rememberMe = make_response()
        response.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug.session'].set(cookie_name, rememberMeKey)
        response.body(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + rememberMeKey + "<br/>")

    response.body("Weak Randomness Test random.randint() executed")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

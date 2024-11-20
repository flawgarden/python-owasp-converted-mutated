
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02504", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    values = request.args.getlist("BenchmarkTest02504")
    param = values[0] if values else ""

    bar = do_something(param)

    r = random.randint(0, 2**31 - 1)
    rememberMeKey = str(r)

    user = "Ingrid"
    fullClassName = __name__
    testCaseNumber = fullClassName.split('.')[-1].replace('BenchmarkTest', '')

    user += testCaseNumber
    cookieName = "rememberMe" + testCaseNumber

    foundUser = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if key == cookieName:
                if value == request.cookies.get(cookieName):
                    foundUser = True

    if foundUser:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
        response.data = (f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>")
        request.cookies[cookieName] = rememberMeKey

    response.data += "Weak Randomness Test random.randint() executed"
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

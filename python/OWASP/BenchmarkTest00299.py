
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00299", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    headers = request.headers.get("BenchmarkTest00299")

    if headers:
        param = headers

    param = os.path.splitext(param)[0]  # Simulate URL decoding

    bar = (7 * 42) - 106 > 200 and "This should never happen" or param

    l = random.getrandbits(64)
    rememberMeKey = str(l)

    user = "Logan"
    fullClassName = __name__
    testCaseNumber = fullClassName.split('.')[-1][len("BenchmarkTest"):]

    user += testCaseNumber
    cookieName = "rememberMe" + testCaseNumber

    foundUser = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies.keys():
            if cookieName == cookie:
                if cookies[cookie] == request.cookies.get(cookieName):
                    foundUser = True

    if foundUser:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug'] = {'session': {cookieName: rememberMeKey}}
        response.data = f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>"

    response.data += "Weak Randomness Test random.getrandbits(64) executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

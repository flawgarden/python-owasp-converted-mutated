
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02521", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'

    param = request.form.getlist("BenchmarkTest02521")
    if param:
        param = param[0]
    else:
        param = ""

    bar = do_something(param)

    try:
        rand = os.urandom(16).hex()
        rememberMeKey = rand[2:]  # Trim off the 0. at the front.

        user = "SafeFloyd"
        fullClassName = benchmark_test.__module__
        testCaseNumber = fullClassName.split('.')[-1].replace("BenchmarkTest", "")

        user += testCaseNumber
        cookieName = "rememberMe" + testCaseNumber

        foundUser = False
        cookies = request.cookies
        if cookies:
            for cookieName in cookies:
                if cookieName == cookieName and cookies[cookieName] == request.cookies.get(cookieName):
                    foundUser = True
                    break

        if foundUser:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
            request.cookies[cookieName] = rememberMeKey
            response.data = (f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.nextFloat() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00298", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.getlist("BenchmarkTest00298")

    if headers:
        param = headers[0]

    param = urllib.parse.unquote(param)

    bar = (7 * 42) - 106 > 200 and "This should never happen" or param

    randNumber = random.randint(0, 98)
    rememberMeKey = str(randNumber)

    user = "Inga"
    fullClassName = benchmark_test.__module__
    testCaseNumber = fullClassName.split('.')[-1][len("BenchmarkTest"):]

    user += testCaseNumber
    cookieName = "rememberMe" + testCaseNumber

    foundUser = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies:
            if cookie == cookieName and request.cookies[cookie] == request.session.get(cookieName):
                foundUser = True

    if foundUser:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
        request.session[cookieName] = rememberMeKey
        response.set_data(user + " has been remembered with cookie: " + cookieName + " whose value is: " + rememberMeKey + "<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.randint executed")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

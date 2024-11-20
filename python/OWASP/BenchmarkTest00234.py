
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00234", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Encoding", "Accept-Language", "Connection"]:  # Add common headers here
            continue
        
        param = name
        break

    bar = "safe!"
    map35995 = {
        "keyA-35995": "a_Value",
        "keyB-35995": param,
        "keyC": "another_Value"
    }
    
    bar = map35995["keyB-35995"]
    bar = map35995["keyA-35995"]

    randNumber = os.urandom(4)  # Generate a random number using os.urandom
    rememberMeKey = str(int.from_bytes(randNumber, 'big') % 99)

    user = "Inga"
    fullClassName = __name__
    testCaseNumber = fullClassName.split('.')[-1][len("BenchmarkTest"):]

    user += testCaseNumber
    cookieName = "rememberMe" + testCaseNumber

    foundUser = False
    cookies = request.cookies
    if cookieName in cookies:
        if cookies[cookieName] == request.environ.get(cookieName):
            foundUser = True

    if foundUser:
        response.data = f"Welcome back: {user}<br/>".encode('utf-8')
    else:
        response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
        request.environ[cookieName] = rememberMeKey
        response.data = f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>".encode('utf-8')

    response.data += "Weak Randomness Test os.urandom executed".encode('utf-8')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

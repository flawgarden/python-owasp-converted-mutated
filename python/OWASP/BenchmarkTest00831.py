
import os
from flask import Flask, request, render_template, make_response
import base64
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00831", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        queryString = request.query_string.decode('utf-8')
        paramval = "BenchmarkTest00831="
        paramLoc = queryString.find(paramval)
        if paramLoc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest00831' in query string."

        param = queryString[paramLoc + len(paramval):]
        ampersandLoc = queryString.find("&", paramLoc)
        if ampersandLoc != -1:
            param = queryString[paramLoc + len(paramval):ampersandLoc]

        param = param.replace('%20', ' ')  # Decoding URL-encoded spaces

        a97193 = param
        b97193 = a97193 + " SafeStuff"
        b97193 = b97193[:-5] + "Chars"  # replace "Chars"

        map97193 = {}
        map97193["key97193"] = b97193
        c97193 = map97193["key97193"]
        d97193 = c97193[:-1]

        e97193 = base64.b64decode(base64.b64encode(d97193.encode())).decode()  # B64 encode and decode
        f97193 = e97193.split(" ")[0]

        # Static aspect
        g97193 = "barbarians_at_the_gate"
        thing = None  # Placeholder for the helper interface
        if thing:
            bar = thing.doSomething(g97193)  # reflection, if implemented

        try:
            randNumber = random.randint(0, 98)
            rememberMeKey = str(randNumber)

            user = "SafeInga"
            fullClassName = type(request).__module__ + '.' + type(request).__name__
            testCaseNumber = fullClassName.split('.')[-1][len("BenchmarkTest"):]

            user += testCaseNumber
            cookieName = "rememberMe" + testCaseNumber

            foundUser = False
            cookies = request.cookies
            if cookies:
                for key, value in cookies.items():
                    if cookieName == key:
                        if value == request.cookies.get(cookieName):
                            foundUser = True

            if foundUser:
                return f"Welcome back: {user}<br/>"
            else:
                rememberMe = make_response()
                rememberMe.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
                request.session[cookieName] = rememberMeKey
                return f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>"

        except Exception as e:
            print("Problem executing SecureRandom.nextInt(int) - TestCase")
            raise e

    return "Weak Randomness Test executed."

if __name__ == "__main__":
    app.run(host='0.0.0.0')

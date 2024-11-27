
import os
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'

@app.route("/weakrand-01/BenchmarkTest00485", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get('BenchmarkTest00485', '')

    thing = ThingFactory.create_thing()
    bar = thing.do_something(param)

    randNumber = random.randint(0, 99)
    rememberMeKey = str(randNumber)

    user = "Inga"
    fullClassName = benchmark_test.__module__ + '.' + benchmark_test.__name__
    testCaseNumber = fullClassName.split('.')[-1].replace('BenchmarkTest', '')

    user += testCaseNumber
    cookieName = "rememberMe" + testCaseNumber

    foundUser = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookieName == cookie:
                if cookies[cookie] == session.get(cookieName):
                    foundUser = True

    if foundUser:
        response.data = f"Welcome back: {user}<br/>"
    else:
        rememberMe = make_response()
        rememberMe.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
        session[cookieName] = rememberMeKey
        response.data = f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>"

    response.data += "Weak Randomness Test random.randint(0, 99) executed"
    return response

class ThingFactory:
    @staticmethod
    def create_thing():
        # Replace this with actual implementation
        return ThingInterface()

class ThingInterface:
    def do_something(self, param):
        # Replace this with actual implementation
        return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')

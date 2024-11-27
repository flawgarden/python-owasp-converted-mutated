
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00185", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.headers.get("BenchmarkTest00185", "")
    param = os.path.basename(param)  # Simulating URL decoding

    bar = "safe!"
    map60659 = {
        "keyA-60659": "a_Value",
        "keyB-60659": param,
        "keyC": "another_Value"
    }
    bar = map60659["keyB-60659"]
    bar = map60659["keyA-60659"]

    try:
        randNumber = random.randint(0, 98)
        rememberMeKey = str(randNumber)

        user = "SafeInga"
        fullClassName = benchmark_test.__module__
        testCaseNumber = fullClassName.split('.')[-1][len("BenchmarkTest"):]
        user += testCaseNumber

        cookieName = "rememberMe" + testCaseNumber

        foundUser = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookieName == cookie:
                    if cookies[cookie] == request.environ.get('session').get(cookieName):
                        foundUser = True

        if foundUser:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True)
            request.environ.get('session')[cookieName] = rememberMeKey
            response.set_data(f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>")
    except Exception as e:
        print("Problem executing SecureRandom.nextInt(int) - TestCase")
        raise e

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

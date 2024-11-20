
from flask import Flask, request, make_response, render_template
import base64
import random
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00186", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    
    param = request.headers.get("BenchmarkTest00186", "")
    param = base64.urlsafe_b64decode(param.encode()).decode('utf-8')

    a18509 = param
    b18509 = a18509 + " SafeStuff"
    b18509 = b18509[:-len("Chars")] + "Chars"
    map18509 = {"key18509": b18509}
    c18509 = map18509["key18509"]
    d18509 = c18509[:-1]
    e18509 = base64.b64decode(base64.b64encode(d18509.encode())).decode()
    f18509 = e18509.split(" ")[0]
    
    thing = None  # This line needs to create a ThingInterface instance
    g18509 = "barbarians_at_the_gate"
    bar = thing.doSomething(g18509) if thing else None 

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
            for cookie in cookies:
                if cookieName == cookie and request.cookies[cookie] == request.args.get(cookieName):
                    foundUser = True
                    break

        if foundUser:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookieName, rememberMeKey, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookieName} whose value is: {rememberMeKey}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextInt(int) - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

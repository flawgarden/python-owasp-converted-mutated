
import os
import base64
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)

@app.route("/weakrand-00/BenchmarkTest00182", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    param = request.headers.get("BenchmarkTest00182", "")
    param = param.encode('utf-8').decode('utf-8')

    a48649 = param
    b48649 = a48649 + " SafeStuff"
    b48649 = b48649[:-5] + "Chars"
    map48649 = {'key48649': b48649}
    c48649 = map48649['key48649']
    d48649 = c48649[:-1]
    e48649 = base64.b64decode(base64.b64encode(d48649.encode())).decode()
    f48649 = e48649.split(" ")[0]
    
    # Dummy implementation for ThingInterface and ThingFactory
    class ThingInterface:
        @staticmethod
        def doSomething(input):
            return input

    class ThingFactory:
        @staticmethod
        def createThing():
            return ThingInterface()

    thing = ThingFactory.createThing()
    g48649 = "barbarians_at_the_gate"
    bar = thing.doSomething(g48649)

    try:
        stuff = random.SystemRandom().gauss(0, 1)
        remember_me_key = str(stuff).split('.')[1]

        user = "SafeGayle"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print(f"Problem executing SecureRandom.nextGaussian() - TestCase: {e}")

    response.data += "Weak Randomness Test random.SystemRandom().gauss() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

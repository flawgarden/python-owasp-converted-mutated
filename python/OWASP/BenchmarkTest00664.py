
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00664", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.args.get("BenchmarkTest00664", "")

    a87833 = param
    b87833 = a87833 + " SafeStuff"
    b87833 = b87833[:-5] + "Chars"
    
    map87833 = {"key87833": b87833}
    c87833 = map87833["key87833"]
    d87833 = c87833[:-1]
    e87833 = base64.b64decode(base64.b64encode(d87833.encode())).decode()

    f87833 = e87833.split(" ")[0]
    thing = create_thing()
    g87833 = "barbarians_at_the_gate"
    bar = thing.do_something(g87833)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]

        user = "SafeFloyd"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split(".")[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response = "Welcome back: {}<br/>".format(user)
        else:
            response += "{} has been remembered with cookie: {} whose value is: {}<br/>".format(
                user, cookie_name, remember_me_key
            )
            response += "Weak Randomness Test java.security.SecureRandom.nextFloat() executed"

            resp_cookie = make_response(response)
            resp_cookie.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return resp_cookie

    except Exception as e:
        print("Problem executing SecureRandom - TestCase")
        raise e

    return response

def create_thing():
    class Thing:
        def do_something(self, input):
            return input[::-1]  # Example of processing input

    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

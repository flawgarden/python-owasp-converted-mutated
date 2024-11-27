
import os
from flask import Flask, request, render_template, make_response
import random
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/weakrand-04/BenchmarkTest01854", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("weakrand-04/BenchmarkTest01854.html"))
        resp.set_cookie("BenchmarkTest01854", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if 'BenchmarkTest01854' in cookies:
            param = cookies['BenchmarkTest01854']

        bar = do_something(request, param)

        rand = random.random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front

        user = "Floyd"
        test_case_number = "01854"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            resp = make_response(
                f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            )
            resp.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path, domain=request.host)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            return resp

    return "Weak Randomness Test executed"

def do_something(request, param):
    a34242 = param  # assign
    b34242 = f"{a34242} SafeStuff"  # stick in string
    b34242 = b34242[:-4] + "Chars"  # replace some of the end content
    map34242 = {}
    map34242["key34242"] = b34242  # put in a collection
    c34242 = map34242["key34242"]  # get it back out
    d34242 = c34242[:-1]  # extract most of it
    e34242 = base64.b64decode(base64.b64encode(d34242.encode())).decode()  # B64 encode and decode it
    f34242 = e34242.split(" ")[0]  # split it on a space

    thing = create_thing()
    g34242 = "barbarians_at_the_gate"  # This is static so this whole flow is 'safe'
    bar = thing.do_something(g34242)  # reflection

    return bar

def create_thing():
    class ThingInterface:
        def do_something(self, input):
            return input[::-1]  # Example behavior (reversing input)

    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

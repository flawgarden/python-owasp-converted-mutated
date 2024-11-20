
import os
import random
from flask import Flask, request, render_template, make_response
from urllib.parse import urlparse
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02497", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    values = request.args.getlist("BenchmarkTest02497")
    param = values[0] if values else ""

    bar = do_something(request, param)

    value = random.random()
    remember_me_key = str(value)[2:]  # Trim off the 0. at the front.

    user = "Donna"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1]  # Extracting class name
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=urlparse(request.url).netloc, path=request.path)
        response = remember_me
        request.cookies[cookie_name] = remember_me_key  # simulate session-based cookie storage

    response.data += "Weak Randomness Test random.random() executed"
    return response

def do_something(request, param):
    a40533 = param  # assign
    b40533 = a40533 + " SafeStuff"  # append some safe content
    b40533 = b40533[:-1] + "Chars"  # replace some of the end content
    map40533 = {"key40533": b40533}  # put in a collection
    c40533 = map40533["key40533"]  # get it back out
    d40533 = c40533[:-1]  # extract most of it
    e40533 = base64.b64decode(base64.b64encode(d40533.encode())).decode()  # B64 encode and decode it
    f40533 = e40533.split(" ")[0]  # split it on a space
    thing = "barbarians_at_the_gate"  # This is static so this whole flow is 'safe'
    bar = "Dummy response for reflection process"  # Placeholder for the reflection logic

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

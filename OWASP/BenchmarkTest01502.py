
import os
import random
from flask import Flask, request, render_template, make_response
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


class Test:
    @staticmethod
    def do_something(request, param):
        a43640 = param
        b43640 = a43640 + " SafeStuff"
        b43640 = b43640[:-5] + "Chars"
        map43640 = {'key43640': b43640}
        c43640 = map43640['key43640']
        d43640 = c43640[:-1]
        e43640 = b64decode(b64encode(d43640.encode())).decode()
        f43640 = e43640.split(" ")[0]
        g43640 = "barbarians_at_the_gate"
        return g43640


@app.route("/weakrand-03/BenchmarkTest01502", methods=['GET', 'POST'])
def benchmark_test():
    param = request.args.get("BenchmarkTest01502", "")
    bar = Test.do_something(request, param)

    value = random.random()
    remember_me_key = str(value).split('.')[1]

    user = "Doug"
    test_case_number = "BenchmarkTest01502"
    user += test_case_number

    cookie_name = f"rememberMe{test_case_number}"

    found_user = False
    cookies = request.cookies
    if cookie_name in cookies:
        if cookies[cookie_name] == request.cookies.get(cookie_name):
            found_user = True

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
        return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>" + \
               "Weak Randomness Test random.random() executed"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

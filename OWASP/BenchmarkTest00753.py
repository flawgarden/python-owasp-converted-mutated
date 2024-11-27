
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def create_thing():
    # Placeholder for actual implementation
    return ThingInterface()

class ThingInterface:
    def doSomething(self, param):
        return param

@app.route("/weakrand-01/BenchmarkTest00753", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    values = request.form.getlist("BenchmarkTest00753")
    param = values[0] if values else ""

    thing = create_thing()
    bar = thing.doSomething(param)

    try:
        l = random.getrandbits(64)
        remember_me_key = str(l)

        user = "SafeLogan"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for name, value in cookies.items():
                if cookie_name == name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {remember_me.name} whose value is: {remember_me.value}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextLong() - TestCase", e)
        raise

    response.data += "Weak Randomness Test random.getrandbits(64) executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

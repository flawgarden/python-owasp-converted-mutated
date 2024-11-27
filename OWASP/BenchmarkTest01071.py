
import os
import base64
import random
import flask
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01071", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01071", "")

    param = flask.request.args.get("BenchmarkTest01071", "")

    bar = Test().do_something(param)

    try:
        numGen = random.SystemRandom()

        # Get 40 random bytes
        random_bytes = numGen.getrandbits(40 * 8).to_bytes(40, 'big')
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == flask.session.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            return "Welcome back: " + user + "<br/>"
        else:
            response = make_response(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            flask.session[cookie_name] = remember_me_key
            return response
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        return str(e)
    finally:
        print("Randomness Test executed")

class Test:
    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

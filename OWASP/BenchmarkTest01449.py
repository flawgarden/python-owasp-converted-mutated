
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01449", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01449":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    try:
        num_gen = os.urandom(8)  # Use a secure random generator
        rand = get_next_number()

        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonatella"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            response.set_cookie(cookie_name, remember_me_key)

    except Exception as e:
        print("Problem executing SecureRandom - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

def get_next_number():
    return os.urandom(8)  # Example replacement for secure random

class Test:

    def do_something(self, param):
        bar = ""
        if param is not None:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

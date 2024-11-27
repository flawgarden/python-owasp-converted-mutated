
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01611", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    values = request.form.getlist("BenchmarkTest01611")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    try:
        random_bytes = random.getrandbits(40 * 8).to_bytes(40, byteorder='big')
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "01611"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for name, value in cookies.items():
                if cookie_name == name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['session'][cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing random bytes generation - TestCase")
        raise e
    finally:
        response.data += "Randomness Test executed"

    return response

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

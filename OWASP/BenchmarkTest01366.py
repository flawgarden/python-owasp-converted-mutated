
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        num = 106
        return param if (7 * 42) - num <= 200 else "This should never happen"

@app.route("/weakrand-03/BenchmarkTest01366", methods=['GET', 'POST'])
def benchmark_test():
    param = request.args.get('BenchmarkTest01366', '')
    bar = Test().do_something(param)

    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    try:
        random_bytes = random.getrandbits(8 * 40).to_bytes(40, 'big')
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "01366"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode('utf-8')

    except Exception as e:
        print("Problem executing random.getrandbits() - TestCase")
        raise e

    response.data += b"Randomness Test executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

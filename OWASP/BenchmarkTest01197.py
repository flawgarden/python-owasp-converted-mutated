
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01197", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest01197", "")
    param = param.encode('utf-8').decode('utf-8')

    bar = Test().do_something(request, param)

    try:
        secure_random_generator = random.SystemRandom()

        # Get 40 random bytes
        random_bytes = secure_random_generator.getrandbits(8 * 40).to_bytes(40, byteorder='big')

        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise

    response.data += "Randomness Test executed"
    return response

class Test:

    def do_something(self, request, param):
        sbxyz6066 = str(param)
        bar = sbxyz6066 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

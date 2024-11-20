
from flask import Flask, request, make_response, render_template
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01448", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'

    param = ""
    flag = True
    for name in request.args.keys():
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01448":
                    param = name
                    flag = False
                    break

    bar = Test().do_something(request, param)

    try:
        rand = random.SystemRandom().random()  # Secure random
        remember_me_key = str(rand)[2:]

        user = "SafeDonna"
        full_class_name = type(benchmark_test).__module__ + "." + type(benchmark_test).__name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

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
            response.data = f"Welcome back: {user}<br/>".encode('utf-8')

        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: {cookie_name} "
                             f"whose value is: {remember_me_key}<br/>").encode('utf-8')

    except Exception as e:
        print("Problem executing SecureRandom - TestCase")
        raise e

    response.data += b"Weak Randomness Test executed"
    return response

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

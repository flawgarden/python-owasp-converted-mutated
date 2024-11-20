
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01372", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.values.get("BenchmarkTest01372", "")

    bar = Test().do_something(request, param)

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-2][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = (
                f"{user} has been remembered with cookie: "
                f"{remember_me.name} whose value is: {remember_me_key}<br/>"
            )

    except Exception as e:
        print("Problem executing SecureRandom.randint() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.SystemRandom().randint() executed"
    return response

class Test:

    def do_something(self, request, param):
        # Simple condition that assigns param to bar on false condition
        num = 106
        bar = param if (7 * 42) - num <= 200 else "This should never happen"
        return bar

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

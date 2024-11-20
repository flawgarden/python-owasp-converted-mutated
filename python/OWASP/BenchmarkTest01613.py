
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01613", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    values = request.form.getlist("BenchmarkTest01613")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__qualname__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            response.data = "Welcome back: " + user + "<br/>"
        else:
            remember_me_cookie = make_response()
            remember_me_cookie.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        
    except Exception as e:
        print("Problem executing SecureRandom.nextInt() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.SystemRandom().randint() executed"
    return response

class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response, render_template
import random
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-02/BenchmarkTest01272", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    param = request.args.get('BenchmarkTest01272', '')

    bar = Test().do_something(param)

    stuff = random.gauss(0, 1)
    remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

    user = "Gayle"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
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
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.gauss() executed"
    
    return response


class Test:
    def do_something(self, param):
        bar = html.escape(param)
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

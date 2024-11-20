
import os
import random
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01700", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01700="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter 'BenchmarkTest01700' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    try:
        rand = get_next_number()
        remember_me_key = str(rand).lstrip('0.')

        user = "SafeDonatella"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies

        if cookies:
            for key, value in cookies.items():
                if key == cookie_name and value == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            response.data += f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise e

    response.data += "Weak Randomness Test executed"
    return response

def get_next_number():
    return random.random()

class Test:

    def do_something(self, param):
        bar = None
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

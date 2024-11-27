
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import random
import secrets

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01699", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01699="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01699' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    try:
        rand = get_next_number()

        remember_me_key = str(rand).split('.')[1]

        user = "SafeDonatella"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name and cookie_value == request.session.get(cookie_name):
                    found_user = True

        response = make_response()
        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            response = remember_me

        return response

    except Exception as e:
        return "Problem executing SecureRandom.nextDouble() - TestCase"

def get_next_number():
    return secrets.randbelow(1000000) / 1000000.0

class Test:

    def do_something(self, param):
        bar = param.replace("<", "&lt;").replace(">", "&gt;")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

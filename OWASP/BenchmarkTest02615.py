
import os
from flask import Flask, request, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02615", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02615="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02615' in query string."

    param = query_string[param_loc + len(paramval):]  # Assumes parameter is last
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    try:
        rand = random.Random().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies.keys():
                if cookie_name == cookie:
                    found_user = True  # Cookie check logic can be added

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = app.make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return response
    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise

def do_something(param):
    return urllib.parse.quote(param)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

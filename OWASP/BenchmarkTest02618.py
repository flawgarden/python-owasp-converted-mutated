
import os
from flask import Flask, request, render_template
import urllib.parse
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02618", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02618="
    paramLoc = query_string.find(paramval)

    if paramLoc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02618' in query string."

    param = query_string[paramLoc + len(paramval):]
    ampersandLoc = query_string.find("&", paramLoc)
    
    if ampersandLoc != -1:
        param = query_string[paramLoc + len(paramval):ampersandLoc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    rand = random.SystemRandom().random()
    remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.
    user = "SafeDonna"
    test_case_number = "02618"
    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
        return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

def do_something(param):
    num = 196
    if (500 / 42) + num > 200:
        return param
    else:
        return "This should never happen"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import os
import random
import string

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02164", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    
    param = request.args.get("BenchmarkTest02164", "")
    bar = do_something(param)

    try:
        l = random.getrandbits(64)
        remember_me_key = str(l)

        user = "SafeLogan"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie == cookie_name:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        raise Exception("Problem executing SecureRandom.nextLong() - TestCase") from e
    
    response.data += "Weak Randomness Test executed"
    return response

def do_something(param):
    return escape(param)

def escape(param):
    return ''.join(c if c.isalnum() or c in ['-', '_'] else '_' for c in param)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

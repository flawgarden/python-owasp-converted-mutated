
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02425", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest02425", "")
    bar = do_something(param)

    r = os.urandom(4).hex()  # Using os.urandom for random value
    remember_me_key = str(r)

    user = "Ingrid"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
        request.cookies[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test executed"
    return response

def do_something(param):
    return param  # Simulating ESAPI encoding (you might want to replace this with actual encoding)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

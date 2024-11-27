
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-06/BenchmarkTest02719", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = make_response()
    param = request.args.get("BenchmarkTest02719")

    bar = do_something(request, param)

    r = random.SystemRandom().randint(0, 2147483647)
    remember_me_key = str(r)

    user = "SafeIngrid"
    test_case_number = "BenchmarkTest02719"
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
        response.data += f"Welcome back: {user}<br/>".encode('utf-8')
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.cookies[cookie_name] = remember_me_key
        response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode('utf-8')

    response.data += b"Weak Randomness Test executed"
    return response

def do_something(request, param):
    bar = "safe!"
    map_ = {
        "keyA-75503": "a_Value",  # put some stuff in the collection
        "keyB-75503": param,      # put it in a collection
        "keyC": "another_Value"    # put some stuff in the collection
    }
    bar = map_["keyB-75503"]  # get it back out
    bar = map_["keyA-75503"]  # get safe value back out

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

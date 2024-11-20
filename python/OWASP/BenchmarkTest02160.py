
import os
import random
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02160", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02160", "")
    bar = do_something(param)

    try:
        num_gen = random.SystemRandom()
        rand = get_next_number(num_gen)

        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.
        user = "SafeDonatella"
        full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
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
            return f"Welcome back: {user}<br/>"
        else:
            response_value = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            response = app.make_response(response_value)
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            return response

    except Exception as e:
        raise Exception("Problem executing SecureRandom.nextDouble() - TestCase") from e

def get_next_number(generator):
    return generator.random()

def do_something(param):
    bar = "safe!"
    map_data = {
        "keyA-25458": "a_Value",  # put some stuff in the collection
        "keyB-25458": param,  # put it in a collection
        "keyC": "another_Value"  # put some stuff in the collection
    }
    bar = map_data["keyB-25458"]  # get it back out
    bar = map_data["keyA-25458"]  # get safe value back out
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

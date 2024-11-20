
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/weakrand-05/BenchmarkTest02348", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02348":
                    param = name
                    flag = False
                    break

    bar = do_something(request, param)

    try:
        rand_number = random.SystemRandom().randint(0, 98)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = benchmark_test.__qualname__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key in cookies:
                if cookie_name == cookie_key:
                    if cookies[cookie_key] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.set_data("Welcome back: " + user + "<br/>")
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.randint() - TestCase")
        raise e

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

def do_something(request, param):
    bar = "safe!"
    map_ = {}
    map_["keyA-48532"] = "a-Value"
    map_["keyB-48532"] = param
    map_["keyC"] = "another-Value"
    bar = map_.get("keyB-48532")

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

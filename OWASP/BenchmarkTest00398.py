
import os
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00398", methods=['GET', 'POST'])
def benchmark_test():
    param = request.args.get('BenchmarkTest00398', '')

    bar = "safe!"
    map_43631 = {}
    map_43631["keyA-43631"] = "a_Value"
    map_43631["keyB-43631"] = param
    map_43631["keyC"] = "another_Value"
    bar = map_43631.get("keyB-43631")
    bar = map_43631.get("keyA-43631")

    value = random.random()
    remember_me_key = str(value).split('.')[1]

    user = "Donna"
    full_class_name = benchmark_test.__qualname__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if cookie_name == key:
                if value == request.session.get(cookie_name):
                    found_user = True
                    break

    response = make_response()
    if found_user:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.session[cookie_name] = remember_me_key
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
    
    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.random() executed")
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

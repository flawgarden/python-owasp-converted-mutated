
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00585", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    flag = True
    for name in request.args.keys():
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00585":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    sbxyz49441 = param + "_SafeStuff"

    rand_number = random.randint(0, 99)
    remember_me_key = str(rand_number)

    user = "SafeInga"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
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
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.randint executed")

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

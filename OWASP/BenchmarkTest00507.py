
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00507", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    map = request.values
    param = ""
    if map:
        values = map.getlist("BenchmarkTest00507")
        if values:
            param = values[0]

    bar = ""
    if param:
        bar = param.split(" ")[0]

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        rememberMeKey = str(r)

        user = "SafeIngrid"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, rememberMeKey, httponly=True, secure=True, path=request.path)
            request.environ['wsgi.session'][cookie_name] = rememberMeKey
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.randint() - TestCase")
        raise e

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.SystemRandom().randint() executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

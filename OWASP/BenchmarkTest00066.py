
import os
from flask import Flask, request, render_template, make_response
import random
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00066", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-00/BenchmarkTest00066.html"))
        user_cookie = ('BenchmarkTest00066', 'anything', 60 * 3, request.path,
                       request.host)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2],
                            path=user_cookie[3], domain=user_cookie[4], secure=True)
        return response

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00066' in cookies:
            param = unquote(cookies['BenchmarkTest00066'])

        bar = "This_should_always_happen" if (7 * 42) - 86 > 200 else param
        value = random.random()
        remember_me_key = str(value)[2:]

        user = "Doug"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = make_response()
            remember_me = (cookie_name, remember_me_key, request.path,
                            request.host)
            response.set_cookie(remember_me[0], remember_me[1], path=remember_me[2],
                                domain=remember_me[3], secure=True, httponly=True)
            response.set_cookie(cookie_name, remember_me_key)
            return (f"{user} has been remembered with cookie: {remember_me[0]} "
                    f"whose value is: {remember_me[1]}<br/>"
                    "Weak Randomness Test executed")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

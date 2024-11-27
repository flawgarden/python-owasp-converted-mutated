
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00320", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    
    headers = request.headers.get("BenchmarkTest00320")
    if headers:
        param = headers

    param = base64.urlsafe_b64decode(param).decode('utf-8')

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        l = random.SystemRandom().randint(0, 2**63 - 1)
        remember_me_key = str(l)

        user = "SafeLogan"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for name, value in cookies.items():
                if cookie_name == name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.nextLong() - TestCase")
        return str(e), 500
    
    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

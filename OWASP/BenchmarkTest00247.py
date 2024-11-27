
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00247", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    param = ""
    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Encoding", "Accept-Language", "Connection"]:  # common headers
            continue
        
        param = name
        break

    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + "Z"

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.environ.get(cookie_name):
                    found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ[cookie_name] = remember_me_key
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        return str(e), 500

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.SystemRandom().random() executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

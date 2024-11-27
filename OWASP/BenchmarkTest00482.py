
import os
import random
import base64
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Required for session management
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00482", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = request.args.get('BenchmarkTest00482', '')

    bar = param

    bytes_random = bytearray(random.getrandbits(8) for _ in range(10))
    remember_me_key = base64.b64encode(bytes_random).decode('utf-8')

    user = "Byron"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        if cookie_name in cookies:
            if cookies[cookie_name] == session.get(cookie_name):
                found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        session[cookie_name] = remember_me_key
        response.data = (
            f"{user} has been remembered with cookie: "
            f"{cookie_name} whose value is: {remember_me_key}<br/>"
        )

    response.data += "Weak Randomness Test executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

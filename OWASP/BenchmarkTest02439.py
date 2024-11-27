
import os
from flask import Flask, request, render_template, make_response
import secrets

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02439", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.args.get("BenchmarkTest02439", "")
    bar = do_something(param)

    try:
        random_bytes = secrets.token_bytes(40)
        remember_me_key = secrets.token_urlsafe()

        user = "SafeByron"
        test_case_number = "02439"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name in cookies:
                if cookie_name == cookie_name:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        response.data = f"Problem executing SecureRandom.nextBytes() - TestCase: {str(e)}"

    response.data += "Randomness Test executed"
    return response

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

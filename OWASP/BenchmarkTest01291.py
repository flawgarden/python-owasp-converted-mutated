
import os
import base64
import secrets
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01291", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get('BenchmarkTest01291', '')

    bar = Test().do_something(request, param)

    try:
        random_bytes = secrets.token_bytes(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "01291"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>").encode('utf-8')

    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        response.data = str(e).encode('utf-8')

    response.data += b"Randomness Test executed"
    return response

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1] + "Z"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

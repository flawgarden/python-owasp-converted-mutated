
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00249", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    for header in request.headers:
        if header in ['Content-Type', 'Accept', 'User-Agent']:
            continue

        param = header
        break

    bar = escape(param)

    try:
        l = random.getrandbits(64)
        remember_me_key = str(l)

        user = "SafeLogan"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key, cookie_value in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.server.shutdown']  # Simulate setting session attribute
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextLong() - TestCase")
        return str(e), 500

    response.data += "Weak Randomness Test executed"
    return response

def escape(text):
    return ''.join(['&lt;' if c == '<' else '&gt;' if c == '>' else c for c in text])

if __name__ == '__main__':
    app.run(host='0.0.0.0')

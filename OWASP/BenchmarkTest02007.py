
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02007", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    for name in request.headers:
        if name in common_headers:
            continue
        param = name
        break

    bar = do_something(request, param)

    try:
        random_bytes = random.getrandbits(40 * 8).to_bytes(40, 'big')
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "BenchmarkTest02007"
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.environ.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ[cookie_name] = remember_me_key
            response.data = user + f" has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        response.data = "Problem executing random bytes generation - TestCase"
        raise

    response.data += "Randomness Test executed"
    return response

def do_something(request, param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

common_headers = ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Authorization',
                  'Cache-Control', 'Connection', 'Content-Length', 'Content-Type', 'Date',
                  'Expect', 'Host', 'If-Modified-Since', 'If-None-Match', 'Range',
                  'Referer', 'User-Agent']

if __name__ == "__main__":
    app.run(host='0.0.0.0')

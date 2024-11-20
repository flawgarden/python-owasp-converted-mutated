
import os
import random
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01999", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        param = ""
        names = request.headers.keys()
        for name in names:
            if name in common_headers():  # Function to check for standard headers
                continue
            param = name
            break
        
        bar = do_something(param)

        bytes_value = bytearray(random.getrandbits(8) for _ in range(10))
        remember_me_key = base64.b64encode(bytes_value).decode('utf-8')

        user = "Byron"
        class_name = benchmark_test.__qualname__
        test_case_number = class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie == cookie_name:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = app.response_class()
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True,
                                domain=request.host, path=request.path)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        return "Weak Randomness Test random.getrandbits() executed"

def do_something(param):
    bar = "safe!"
    map28743 = {}
    map28743["keyA-28743"] = "a-Value"
    map28743["keyB-28743"] = param
    map28743["keyC"] = "another-Value"
    bar = map28743["keyB-28743"]
    return bar

def common_headers():
    return set(['Host', 'User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding',
                'Connection', 'Upgrade-Insecure-Requests', 'DNT', 'Cache-Control'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')

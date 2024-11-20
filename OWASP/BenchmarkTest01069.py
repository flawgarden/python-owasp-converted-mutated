
import os
from flask import Flask, request, render_template, make_response
import base64
import secrets
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01069", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("BenchmarkTest01069") is not None:
        param = request.headers.get("BenchmarkTest01069")

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        random_bytes = secrets.token_bytes(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = __name__ + '.benchmark_test'
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['session'][cookie_name] = remember_me_key
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e
    finally:
        response.set_data(response.get_data(as_text=True) + "Randomness Test executed")

    return response

class Test:

    def do_something(self, request, param):
        bar = self.escape_html(param)
        return bar

    def escape_html(self, param):
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

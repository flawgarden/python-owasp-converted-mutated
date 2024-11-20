
import os
import base64
from flask import Flask, request, render_template, make_response
import random
import secrets

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-04/BenchmarkTest02157", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02157", "")

    bar = do_something(request, param)

    try:
        random_bytes = secrets.token_bytes(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        full_class_name = __name__
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
            response.data += f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
            request.remote_user = remember_me_key
            response.data += f"{user} has been remembered with cookie: {remember_me.cookie} whose value is: {remember_me_key}<br/>".encode('utf-8')

    except Exception as e:
        print("Problem executing secrets.token_bytes() - TestCase", e)

    finally:
        response.data += "Randomness Test secrets.token_bytes() executed".encode('utf-8')

    return response


def do_something(request, param):
    bar = ""
    if param:
        bar = base64.b64encode(base64.b64decode(param.encode('utf-8'))).decode('utf-8')
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

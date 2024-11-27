
import os
import base64
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-04/BenchmarkTest02072", methods=['GET', 'POST'])
def benchmark_test_02072():
    if request.method == 'GET':
        return benchmark_test_02072_post()

    return benchmark_test_02072_post()


def benchmark_test_02072_post():
    response_str = ""
    
    param = request.headers.get("BenchmarkTest02072", "")
    param = param.replace("+", " ")  # URL Decode the header value

    bar = do_something(param)

    try:
        random_bytes = bytearray(random.getrandbits(8) for _ in range(40))
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "02072"
        user += test_case_number
        
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                cookie_value = cookies[cookie_name]
                if cookie_value == request.cookies.get(cookie_name):
                    found_user = True
        
        if found_user:
            response_str += "Welcome back: " + user + "<br/>"
        else:
            response = make_response()
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'][cookie_name] = remember_me_key
            response_str += (user + " has been remembered with cookie: " +
                             cookie_name + " whose value is: " + remember_me_key + "<br/>")
            return response_str

    except Exception as e:
        print("Problem executing SecureRandom - TestCase")
        raise e
    finally:
        response_str += "Randomness Test executed"
    
    return response_str


def do_something(param):
    bar = ""
    if param:
        bar = param.split(" ")[0]
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

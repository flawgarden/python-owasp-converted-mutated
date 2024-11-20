
import os
import base64
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
app.secret_key = 'supersecretkey'

@app.route("/weakrand-04/BenchmarkTest01947", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.headers.get("BenchmarkTest01947", "")
    param = param  # URL decoding is not necessary in Flask

    bar = do_something(param)

    try:
        random_bytes = bytearray(random.getrandbits(8) for _ in range(40))
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8').rstrip("=")

        user = "SafeByron"
        test_case_number = "01947"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if cookie_name in request.cookies:
            if request.cookies[cookie_name] == session.get(cookie_name):
                found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e
    finally:
        response.set_data(response.get_data(as_text=True) + "Randomness Test executed")
    
    return response

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")
        bar = values_list[0]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02075", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest02075', '')

    param = base64.b64decode(base64.b64encode(param.encode())).decode()

    bar = do_something(param)

    try:
        num_gen = os.urandom(8)
        rand = get_next_number(num_gen)

        remember_me_key = str(rand)[2:]

        user = "SafeDonatella"
        full_class_name = "BenchmarkTest02075"
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name in cookies:
                if cookie_name == cookie_name:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

        response = make_response()

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

def get_next_number(generator):
    return float.fromhex(generator.hex())  # Simulate randomness

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

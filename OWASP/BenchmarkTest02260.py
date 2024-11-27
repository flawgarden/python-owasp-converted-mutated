
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02260", methods=['GET', 'POST'])
def benchmark_test_02260():
    if request.method == 'GET':
        return benchmark_test_02260()
    else:
        response = make_response()
        param = request.args.get("BenchmarkTest02260", "")
        bar = do_something(param)

        try:
            r = random.SystemRandom().randint(0, 2**31 - 1)
            remember_me_key = str(r)
            user = "SafeIngrid"
            class_name = __name__
            case_number = class_name[class_name.rfind('.') + 1 + len("BenchmarkTest"):]

            user += case_number
            cookie_name = "rememberMe" + case_number
            found_user = False
            cookies = request.cookies

            if cookies:
                if cookie_name in cookies:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

            if found_user:
                response.data = f"Welcome back: {user}<br/>"
            else:
                remember_me = make_response()
                remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                request.cookies[cookie_name] = remember_me_key
                response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        except Exception as e:
            print(f"Problem executing SecureRandom.randint() - TestCase: {e}")
            return str(e)

        response.data += "Weak Randomness Test executed"
        return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

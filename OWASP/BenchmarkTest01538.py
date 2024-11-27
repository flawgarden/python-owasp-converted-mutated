
from flask import Flask, request, make_response, render_template
import os
import random
import base64
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        bar = "safe!"
        map82396 = {}
        map82396["keyA-82396"] = "a_Value"
        map82396["keyB-82396"] = param
        map82396["keyC"] = "another_Value"
        bar = map82396.get("keyB-82396")
        bar = map82396.get("keyA-82396")
        return bar

@app.route("/weakrand-03/BenchmarkTest01538", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = make_response()
        param = request.form.get("BenchmarkTest01538", "")
        bar = Test().do_something(param)

        try:
            secure_random_generator = random.SystemRandom()
            random_bytes = secure_random_generator.getrandbits(40 * 8).to_bytes(40, 'big')
            remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

            user = "SafeByron"
            test_case_number = "BenchmarkTest01538"
            user += test_case_number
            cookie_name = "rememberMe" + test_case_number

            found_user = False
            cookies = request.cookies
            if cookies:
                for cookie in cookies:
                    if cookie_name == cookie:
                        if cookies[cookie_name] == request.cookies.get(cookie_name):
                            found_user = True

            if found_user:
                response.data = f"Welcome back: {user}<br/>"
            else:
                remember_me = make_response()
                remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                request.session[cookie_name] = remember_me_key
                response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        except Exception as e:
            print("Problem executing random key generation - TestCase")
            raise e
        finally:
            response.data += "Randomness Test executed"
            return response

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

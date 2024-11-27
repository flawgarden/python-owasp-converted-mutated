
import os
import base64
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        bar = None
        guess = "ABC"
        switch_target = guess[1]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

@app.route("/weakrand-03/BenchmarkTest01539", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest01539", "")

    bar = Test().do_something(param)

    try:
        random_bytes = random.getrandbits(320)
        remember_me_key = base64.b64encode(random_bytes.to_bytes(40, 'big')).decode('utf-8')

        user = "SafeByron"
        test_case_number = "01539"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie in cookies.keys():
                if cookie_name == cookie:
                    if cookies[cookie] == request.args.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = (cookie_name, remember_me_key, {'httponly': True, 'secure': True, 'path': request.path})
            response.set_cookie(*remember_me)
            response.data = f"{user} has been remembered with cookie: {remember_me[0]} whose value is: {remember_me[1]}<br/>"
    except Exception as e:
        response.data = f"Problem executing SecureRandom.nextBytes() - {str(e)}"

    response.data += "Randomness Test executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

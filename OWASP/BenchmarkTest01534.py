
import os
import random
import base64
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'supersecretkey'  # Required for session management
app.config['DEBUG'] = True

class Test:
    @staticmethod
    def do_something(param):
        num = 106
        return param if (7 * 42) - num <= 200 else "This should never happen"

@app.route("/weakrand-03/BenchmarkTest01534", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    param = request.args.get("BenchmarkTest01534", "")
    bar = Test.do_something(param)

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        response.data = str(e)

    response.data += "Randomness Test os.urandom() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

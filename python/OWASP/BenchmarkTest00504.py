
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00504", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00504', '')

    bar = param  # Here you would normally encode this, left for simplicity.

    try:
        rand = random.SystemRandom().random()  # Using SystemRandom for better randomness.
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeFloyd"
        full_class_name = 'BenchmarkTest00504'  # Mock class name for example
        test_case_number = full_class_name[len('BenchmarkTest'):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        response = make_response()
        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        
        response.data += "Weak Randomness Test random.SystemRandom().random() executed"
        return response
    
    except Exception as e:
        print("Problem executing random.SystemRandom() - TestCase")
        return "An error occurred.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')

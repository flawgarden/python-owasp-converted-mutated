
import os
from flask import Flask, request, render_template, make_response
import random
import string

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00582", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00582":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = "This_should_always_happen" if (7 * 18 + 106) > 200 else param

    try:
        num_gen = random.SystemRandom()
        rand = get_next_number(num_gen)
        remember_me_key = str(rand)[2:]

        user = "SafeDonatella"
        full_class_name = benchmark_test.__module__
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
                        break

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
    return generator.random()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

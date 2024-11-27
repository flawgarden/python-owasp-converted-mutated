
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00752", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = make_response()
    
    values = request.form.getlist("BenchmarkTest00752")
    param = values[0] if values else ""
    
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe
    
    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bob's your uncle"

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            cookie_value = cookies.get(cookie_name)
            if cookie_value == request.session.get(cookie_name):
                found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.randint() - TestCase")
        raise e

    response.data += "Weak Randomness Test executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

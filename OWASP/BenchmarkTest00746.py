
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00746", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
        
    response = make_response()
    values = request.form.getlist("BenchmarkTest00746")
    param = values[0] if values else ""

    bar = ""
    guess = "ABC"
    switchTarget = guess[1]  # condition 'B', which is safe

    if switchTarget == 'A':
        bar = param
    elif switchTarget == 'B':
        bar = "bob"
    elif switchTarget in ('C', 'D'):
        bar = param
    else:
        bar = "bob's your uncle"

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "00746"
        user += test_case_number
        
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.values.get(cookie_name):
                found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        
    except Exception as e:
        print("Problem executing secure random bytes generation - TestCase")
        raise

    response.set_data(response.get_data(as_text=True) + "Randomness Test os.urandom executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

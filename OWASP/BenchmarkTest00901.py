
from flask import Flask, request, render_template, make_response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00901", methods=['GET', 'POST'])
def benchmark_test_00901():
    if request.method == 'GET':
        return benchmark_test_00901()

    response = make_response()
    param = request.args.get("BenchmarkTest00901", "")

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    rand_number = random.randint(0, 98)
    remember_me_key = str(rand_number)

    user = "Inga"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies

    if cookies:
        for name, value in cookies.items():
            if cookie_name == name:
                if value == request.session.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.session[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.randint executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template, session
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key_here'


@app.route("/weakrand-05/BenchmarkTest02337", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02337":
                    param = name
                    flag = False
                    
    bar = do_something(param)

    l = random.getrandbits(64)
    remember_me_key = str(l)

    user = "Logan"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == session.get(cookie_name):
                    found_user = True
                    
    if found_user:
        response.data += f"Welcome back: {user}<br/>"

    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        session[cookie_name] = remember_me_key
        response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.getrandbits(64) executed"
    return response


def do_something(param):
    bar = "safe!"
    map19180 = {
        "keyA-19180": "a_Value",
        "keyB-19180": param,
        "keyC": "another_Value"
    }
    bar = map19180["keyB-19180"]
    bar = map19180["keyA-19180"]

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

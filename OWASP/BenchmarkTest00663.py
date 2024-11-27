
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00663", methods=['GET', 'POST'])
def benchmark_test_00663():
    if request.method == 'GET':
        return benchmark_test_00663()

    param = request.form.get("BenchmarkTest00663", "")
    bar = "safe!"
    map67527 = {
        "keyA-67527": "a-Value",
        "keyB-67527": param,
        "keyC": "another-Value"
    }
    bar = map67527["keyB-67527"]

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]

        user = "SafeDonna"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("benchmark_test_"):]
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie == cookie_name:
                    if request.cookies[cookie_name] == request.cookies[cookie_name]:
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            remember_me.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            return remember_me.get_data()
    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        raise e
    return "Weak Randomness Test random.SystemRandom().random() executed"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00505", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "We should not directly return 'safe!' without validation."
    param = request.args.get('BenchmarkTest00505', default='', type=str)

    bar = "safe!"
    map67557 = {
        "keyA-67557": "a-Value",
        "keyB-67557": param,
        "keyC": "another-Value"
    }
    bar = map67557.get("keyB-67557", bar)

    try:
        rand_number = random.SystemRandom().randint(0, 98)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response_content += f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['session'][cookie_name] = remember_me_key
            response_content += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        return str(e)

    response_content += "Weak Randomness Test executed"
    return response_content

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

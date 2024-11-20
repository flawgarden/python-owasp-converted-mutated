
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01950", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.headers.get("BenchmarkTest01950", "")
    param = os.popen(f"python3 -c 'import urllib.parse; print(urllib.parse.unquote(\"{param}\"))'").read().strip()

    bar = do_something(param)

    try:
        import random
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeFloyd"
        full_class_name = benchmark_test.__module__ + "." + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response += f"Welcome back: {user}<br/>"
        else:
            response += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            response += "Weak Randomness Test random.SystemRandom().random() executed"
            # Set cookie example (not secure or HttpOnly in Flask for simplicity)
            # response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)

    except Exception as e:
        response += "Problem executing SecureRandom.random() - TestCase"
    
    response += "Weak Randomness Test random.SystemRandom().random() executed"
    return response

def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-14411": "a-Value",
        "keyB-14411": param,
        "keyC": "another-Value"
    }
    bar = map_.get("keyB-14411")
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

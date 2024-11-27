
import os
import random
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01614", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return benchmark_test_post()
    return benchmark_test_get()

def benchmark_test_get():
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest01614")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    try:
        l = random.getrandbits(64)
        remember_me_key = str(l)

        user = "SafeLogan"
        full_class_name = __name__
        test_case_number = full_class_name.split(".")[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if cookie_name == key:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            response = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            response += "Weak Randomness Test random.getrandbits(64) executed"
            return response

    except Exception as e:
        print("Problem executing random.getrandbits(64) - TestCase")
        return str(e)

class Test:
    def do_something(self, param):
        bar = self.encode_for_html(param)
        return bar

    def encode_for_html(self, param):
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

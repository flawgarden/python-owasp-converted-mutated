
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)
            bar = values_list[1]
        return bar

@app.route("/weakrand-03/BenchmarkTest01544", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = make_response()
        param = request.args.get("BenchmarkTest01544", "")
        test = Test()
        bar = test.do_something(param)

        try:
            rand = random.SystemRandom().random()
            remember_me_key = str(rand)[2:]

            user = "SafeFloyd"
            test_case_number = "BenchmarkTest01544"
            user += test_case_number

            cookie_name = "rememberMe" + test_case_number

            found_user = False
            if 'rememberMe' in request.cookies:
                cookie_value = request.cookies['rememberMe' + test_case_number]
                if cookie_value == request.cookies.get(cookie_name):
                    found_user = True

            if found_user:
                return f"Welcome back: {user}<br/>"
            else:
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
                return response

        except Exception as e:
            raise Exception("Problem executing SecureRandom.random() - TestCase") from e

        response.data += b"Weak Randomness Test executed"
        return response

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

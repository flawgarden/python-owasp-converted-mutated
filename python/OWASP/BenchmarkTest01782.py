
import os
import random
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01782", methods=['GET', 'POST'])
def benchmark_test():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01782", None)

        bar = Test().do_something(request, param)

        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "Gayle"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False
        cookies = request.cookies

        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key  # Simulating session attribute
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        response.data += "Weak Randomness Test random.gauss() executed"
        return response
    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = ""
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

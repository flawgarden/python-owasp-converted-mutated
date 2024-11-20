
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        # Placeholder for the actual implementation
        return param

@app.route("/weakrand-03/BenchmarkTest01452", methods=['GET', 'POST'])
def benchmark_test_01452():
    if request.method == 'GET':
        return benchmark_test_01452()

    response = make_response()
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        if not flag:
            break
        values = request.args.getlist(name)
        for value in values:
            if value == "BenchmarkTest01452":
                param = name
                flag = False
                break

    bar = Test().do_something(param)

    try:
        stuff = random.gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "SafeGayle"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key in cookies:
                if cookie_name == key:
                    if cookies[key] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)  # Store in session
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print(f"Problem executing random.gauss() - TestCase: {str(e)}")
        raise

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.gauss() executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

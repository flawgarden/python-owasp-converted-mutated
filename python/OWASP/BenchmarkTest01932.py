
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01932", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01932", "")

    param = os.path.basename(param)

    bar = do_something(param)

    r = os.urandom(4)  # Simulate Random
    remember_me_key = str(int.from_bytes(r, 'big'))

    user = "Ingrid"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

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
        response = make_response()
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        return response

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

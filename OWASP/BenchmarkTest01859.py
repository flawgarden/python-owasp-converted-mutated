
import os
from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest01859", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-04/BenchmarkTest01859.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01859", "whatever", max_age=60*3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest01859", "whatever", max_age=60*3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies

        if 'BenchmarkTest01859' in cookies:
            param = cookies.get('BenchmarkTest01859')

        bar = do_something(request, param)
        remember_me_key = str(os.urandom(8).hex())

        user = "Logan"
        full_class_name = "BenchmarkTest01859"
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = cookie_name in request.cookies
        if found_user:
            if request.cookies[cookie_name] == request.environ.get('werkzeug.session').get(cookie_name):
                return f"Welcome back: {user}<br/>"
        else:
            response = make_response()
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ.get('werkzeug.session')[cookie_name] = remember_me_key
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        return "Weak Randomness Test executed"

def do_something(request, param):
    return param.split(" ")[0] if param else ""

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

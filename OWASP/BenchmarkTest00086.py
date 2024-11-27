
from flask import Flask, request, make_response, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00086", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response(render_template("weakrand-00/BenchmarkTest00086.html"))
    
    if request.method == 'GET':
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00086", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response = user_cookie

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00086" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest00086"])

        # Simple if statement that assigns constant to bar on true condition
        num = 86
        bar = "This_should_always_happen" if ((7 * 42) - num > 200) else param

        remember_me_key = str(random.getrandbits(64))

        user = "Logan"
        test_case_number = "00086"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return "Welcome back: " + user + "<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_cookie(cookie_name, remember_me_key)
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

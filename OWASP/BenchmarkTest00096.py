
import os
import random
import string
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00096", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-00/BenchmarkTest00096.html"))
        user_cookie = make_response()
        user_cookie.set_cookie('BenchmarkTest00096', 'whatever', max_age=60*3, secure=True, path=request.path, domain=request.host)
        response.cookies['BenchmarkTest00096'] = user_cookie.value
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00096' in the_cookies:
            param = the_cookies['BenchmarkTest00096']

        bar = param if (7 * 42) - 106 <= 200 else "This should never happen"

        try:
            rand_number = random.randint(0, 98)
            remember_me_key = str(rand_number)

            user = "SafeInga"
            test_case_number = "00096"
            user += test_case_number
            cookie_name = f"rememberMe{test_case_number}"

            found_user = False
            if cookie_name in the_cookies:
                if the_cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

            if found_user:
                return f"Welcome back: {user}<br/>"
            else:
                response = make_response()
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                response.cookies[cookie_name] = remember_me_key
                return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        except Exception as e:
            print("Problem executing SecureRandom.nextInt(int) - TestCase")
            raise

    return "Weak Randomness Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

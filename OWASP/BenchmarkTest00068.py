
from flask import Flask, request, render_template, make_response
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00068", methods=['GET', 'POST'])
def benchmark_test_00068():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-00/BenchmarkTest00068.html"))
        user_cookie = ('BenchmarkTest00068', 'anything', {'max_age': 60 * 3, 'secure': True, 'path': request.path, 'domain': request.host})
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2]['max_age'], secure=user_cookie[2]['secure'], path=user_cookie[2]['path'], domain=user_cookie[2]['domain'])
        return response

    if request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if 'BenchmarkTest00068' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00068'])

        bar = "This_should_always_happen" if (7 * 18 + 106) > 200 else param

        value = random.random()
        remember_me_key = str(value)[2:]  # Trim off the 0. at the front.

        user = "Doug"
        full_class_name = benchmark_test_00068.__module__ + '.' + benchmark_test_00068.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path, domain=request.host)
            request.environ['wsgi.session'][cookie_name] = remember_me_key
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

        return "Weak Randomness Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template, make_response
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00369", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.args.get('BenchmarkTest00369', "")
    bar = param[:-1] if len(param) > 1 else param

    value = random.random()
    remember_me_key = str(value)[2:]

    user = "Doug"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.session.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        return f"Welcome back: {user}<br/>"

    remember_me = make_response()
    remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True,
                            domain=urllib.parse.urlparse(request.url).hostname,
                            path=request.path)
    request.session[cookie_name] = remember_me_key
    remember_me.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    return remember_me


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

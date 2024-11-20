
import os
import secrets
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00577", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00577" and flag:
                    param = name
                    flag = False

    bar = "This_should_always_happen" if (7 * 18) + 106 > 200 else param

    try:
        random_bytes = secrets.token_bytes(40)
        remember_me_key = secrets.token_hex(20)

        user = "SafeByron"
        full_class_name = "BenchmarkTest00577"
        test_case_number = full_class_name[full_class_name.index('BenchmarkTest') + len('BenchmarkTest'):]

        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        response.data = "Problem executing SecureRandom.nextBytes() - TestCase"

    response.data += "Randomness Test executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

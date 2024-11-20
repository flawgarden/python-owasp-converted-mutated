
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-03/BenchmarkTest01297", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return render_template("index.html")


def handle_request(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get("BenchmarkTest01297", "")
    bar = Test().do_something(param)

    try:
        r = random.SystemRandom().randint(0, 2**32 - 1)
        remember_me_key = str(r)

        user = "SafeIngrid"
        test_case_number = "BenchmarkTest01297"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode()
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key
            response.data = (
                f"{user} has been remembered with cookie: "
                f"{remember_me.name} whose value is: {remember_me_key}<br/>"
            ).encode()

    except Exception as e:
        print("Problem executing random.SystemRandom().randint() - TestCase")
        return str(e).encode()

    response.data += "Weak Randomness Test executed".encode()
    return response


class Test:

    def do_something(self, param):
        bar = self.encode_for_html(param)
        return bar

    def encode_for_html(self, param):
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")  # Simple HTML encoding


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

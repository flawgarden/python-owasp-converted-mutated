
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-02/BenchmarkTest01202", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01202", "")
    param = os.popen('echo ' + param + ' | xargs -0 printf "%b"').read()  # URL decode the param

    bar = Test().do_something(param)

    try:
        stuff = random.Random().gauss(0, 1)
        remember_me_key = str(stuff)[2:]

        user = "SafeGayle"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie].encode() == request.cookies.get(cookie_name).encode():
                        found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            return remember_me
    except Exception as e:
        print("Problem executing random.gauss() - TestCase")
        raise e


class Test:

    @staticmethod
    def do_something(param):
        bar = param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

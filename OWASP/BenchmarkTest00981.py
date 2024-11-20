
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def doSomething(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.route("/cmdi-01/BenchmarkTest00981", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00981.html"))
        user_cookie = make_response("Set a cookie for the test")
        user_cookie.set_cookie("BenchmarkTest00981", ".", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest00981", ".", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest00981' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00981'])

        bar = Test().doSomething(param)

        cmd = ""
        a1 = ""
        a2 = ""
        args = []
        os_name = os.name

        if os_name == "nt":
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = "echo "
            args = [a1, a2, cmd + bar]
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = "ls "  # or any suitable command
            args = [a1, a2, cmd + bar]

        args_env = {"foo": "bar"}

        try:
            process = os.popen(" ".join(args))
            result = process.read()
            return result
        except Exception as e:
            return f"Problem executing cmd - TestCase: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

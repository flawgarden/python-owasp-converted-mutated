
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-01/BenchmarkTest00983", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00983.html"))
        user_cookie = make_response("FOO=echo Injection")
        user_cookie.set_cookie("BenchmarkTest00983", "FOO%3Decho+Injection", max_age=60 * 3, secure=True)
        response.set_cookie("BenchmarkTest00983", "FOO%3Decho+Injection", max_age=60 * 3, secure=True)
        return response
    else:
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00983' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest00983'])

        bar = Test().do_something(request, param)

        cmd = "your_command_here"  # Replace with your command retrieval logic

        args_env = [bar]
        try:
            process = os.popen(f"{cmd} {' '.join(args_env)}")
            output = process.read()
            return output
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return str(e)


class Test:

    def do_something(self, request, param):
        num = 196
        if (500 / 42) + num > 200:
            return param
        else:
            return "This should never happen"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

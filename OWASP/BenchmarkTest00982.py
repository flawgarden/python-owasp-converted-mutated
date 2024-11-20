
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00982", methods=['GET'])
def benchmark_test_get():
    response = make_response(render_template("cmdi-01/BenchmarkTest00982.html"))
    user_cookie = ("BenchmarkTest00982", "FOO%3Decho+Injection")
    response.set_cookie(user_cookie[0], user_cookie[1], max_age=60 * 3, secure=True, path=request.path,
                        domain=request.host)
    return response

@app.route("/cmdi-01/BenchmarkTest00982", methods=['POST'])
def benchmark_test_post():
    param = "noCookieValueSupplied"
    cookies = request.cookies

    if "BenchmarkTest00982" in cookies:
        param = cookies.get("BenchmarkTest00982")

    bar = Test().do_something(request, param)

    cmd = Utils.get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        return output
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {e}"

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map20875 = {}
        map20875["keyA-20875"] = "a_Value"
        map20875["keyB-20875"] = param
        map20875["keyC"] = "another_Value"
        bar = map20875.get("keyB-20875")
        bar = map20875.get("keyA-20875")
        return bar

class Utils:

    @staticmethod
    def get_insecure_os_command_string():
        return "your_command_here"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

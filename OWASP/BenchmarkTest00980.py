
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00980", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("cmdi-01/BenchmarkTest00980.html"))
        user_cookie = "BenchmarkTest00980=FOO%3Decho+Injection"
        resp.set_cookie("BenchmarkTest00980", "FOO%3Decho+Injection", max_age=60 * 3, secure=True, path=request.path, domain=request.host[:-len(request.environ['SERVER_PORT']) - 1])
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if "BenchmarkTest00980" in the_cookies:
            param = the_cookies.get("BenchmarkTest00980")

        bar = Test().do_something(request, param)
        cmd = Utils.get_insecure_os_command_string()
        args = [cmd]
        args_env = [bar]

        try:
            process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
            result = process.read()
            return result
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return f"Error: {e}"

class Test:
    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)
            bar = values_list[1]
        return bar

class Utils:
    @staticmethod
    def get_insecure_os_command_string():
        # Implementation here to get a command string, as per original logic
        return "your_command_here"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

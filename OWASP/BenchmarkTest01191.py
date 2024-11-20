
from flask import Flask, request, render_template
import subprocess
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        # Placeholder for the logic that generates 'bar'
        bar = self.create_thing().do_something(param)
        return bar

    def create_thing(self):
        return Thing()

class Thing:

    def do_something(self, param):
        # Placeholder for actual implementation of do_something
        return param

@app.route("/cmdi-01/BenchmarkTest01191", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""

    headers = request.headers.getlist("BenchmarkTest01191")
    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        p = subprocess.Popen(args, env={'CMD_ENV': bar}, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        response = output.decode('utf-8')
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = escape_html(str(e))

    return response

def get_insecure_os_command_string():
    # Placeholder for the logic to get a command string
    return "/bin/echo"

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

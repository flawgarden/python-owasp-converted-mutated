
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01192", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""
    headers = request.headers.get("BenchmarkTest01192")

    if headers:
        param = headers  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()

    try:
        p = os.popen(f"{cmd} {bar}")
        response = p.read()
        p.close()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = str(e)

    return response

class Test:
    def do_something(self, request, param):
        bar = ""

        # Simple if statement that assigns param to bar on true condition
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

def get_insecure_os_command_string():
    return "your_command_here"  # replace with actual command logic

if __name__ == "__main__":
    app.run(host='0.0.0.0')

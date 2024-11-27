
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00307", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if "BenchmarkTest00307" in request.headers:
        param = request.headers["BenchmarkTest00307"]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Check for Windows
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        response.data = output
        process.close()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Simple error handling
        return response

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

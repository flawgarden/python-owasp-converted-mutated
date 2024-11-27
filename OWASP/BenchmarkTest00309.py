
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__)

@app.route("/cmdi-00/BenchmarkTest00309", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = ""
    if "BenchmarkTest00309" in request.headers:
        headers = request.headers.getlist("BenchmarkTest00309")
        if headers:
            param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map92785 = {
        "keyA-92785": "a_Value",
        "keyB-92785": param,
        "keyC": "another_Value"
    }
    bar = map92785["keyB-92785"]
    bar = map92785["keyA-92785"]

    cmd = "your_command_here"  # Replace this with your actual command

    args_env = [bar]
    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        output = process.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(urllib.parse.quote(str(e)))
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

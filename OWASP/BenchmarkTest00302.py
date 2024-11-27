
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00302", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    header = request.headers.get("BenchmarkTest00302")

    if header:
        param = header

    param = urllib.parse.unquote(param)

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    cmd = ""
    os_name = os.name
    if os_name == "nt":
        cmd = "echo "

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Simple error handling
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

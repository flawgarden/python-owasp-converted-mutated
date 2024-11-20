
import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00308", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    headers = request.headers.getlist('BenchmarkTest00308')

    if headers:
        param = headers[0]

    param = urllib.parse.unquote(param)

    bar = ''
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    cmd = ''
    os_name = os.name
    if os_name == 'nt':
        cmd = 'echo '  # Windows command

    try:
        process = os.popen(cmd + bar)  # Execute command
        result = process.read()
        response.set_data(result)
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

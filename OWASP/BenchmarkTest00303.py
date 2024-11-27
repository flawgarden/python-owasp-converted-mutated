
import os
import urllib.parse
from flask import Flask, request, render_template, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00303", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest00303", "")
    param = urllib.parse.unquote(param)

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = ""
    a1 = ""
    a2 = ""
    args = []
    os_name = os.name

    if os_name == 'nt':
        a1 = 'cmd.exe'
        a2 = '/c'
        cmd = f'echo {bar}'
        args = [a1, a2, cmd]
    else:
        a1 = 'sh'
        a2 = '-c'
        cmd = f'ping -c1 {bar}'
        args = [a1, a2, cmd]

    try:
        process = os.popen(' '.join(args))
        results = process.read()
        response.set_data(results)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(f'Error: {e}')
        return response

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

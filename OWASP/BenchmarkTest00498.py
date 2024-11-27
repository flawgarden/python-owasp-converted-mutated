
import os
from flask import Flask, request, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00498", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.values.get('BenchmarkTest00498', '')

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = 'your_insecure_command_here'  # Replace with actual method to get the command
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = p.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

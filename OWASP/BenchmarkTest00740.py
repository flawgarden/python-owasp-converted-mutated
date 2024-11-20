
import os
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00740", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    values = request.values.getlist("BenchmarkTest00740")
    param = values[0] if values else ""

    bar = "safe!"
    map87432 = {
        "keyA-87432": "a-Value",
        "keyB-87432": param,
        "keyC": "another-Value"
    }
    bar = map87432.get("keyB-87432")

    cmd = os.getenv('INSECURE_OS_COMMAND')  # Placeholder for insecure command retrieval
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = p.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

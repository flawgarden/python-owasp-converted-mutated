
import os
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00499", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")
    param = request.args.get("BenchmarkTest00499", "")

    bar = param

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "cmd /c echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        result = process.read()
        response.data = result
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Simple way to return error message
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

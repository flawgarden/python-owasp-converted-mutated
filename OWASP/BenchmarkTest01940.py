
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01940", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_type = "text/html;charset=UTF-8"
    param = request.headers.get("BenchmarkTest01940", "")

    param = param # Assuming param should be URL decoded

    bar = do_something(param)

    cmd = ""
    if os.name == "nt":
        cmd = "echo " # Use equivalent command in Windows
        
    args_env = {"Foo": "bar"}
    try:
        process = os.popen(cmd + bar)  # Note: Using os.popen for demonstration
        output = process.read()
        process.close()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

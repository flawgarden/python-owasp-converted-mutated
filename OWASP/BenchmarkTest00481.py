
import os
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00481", methods=['GET', 'POST'])
def benchmark_test_00481():
    if request.method == 'GET':
        return benchmark_test_00481()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get("BenchmarkTest00481", "")

    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    argList = []

    osName = os.name
    if osName == "nt":
        argList.append("cmd.exe")
        argList.append("/c")
    else:
        argList.append("sh")
        argList.append("-c")

    argList.append("echo " + bar)

    pb = os.popen(' '.join(argList))

    try:
        output = pb.read()
        return output
    except Exception as e:
        print("Problem executing cmdi - ProcessBuilder(java.util.List) Test Case")
        raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')

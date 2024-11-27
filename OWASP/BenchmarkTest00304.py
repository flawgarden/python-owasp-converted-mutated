
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00304", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""
    headers = request.headers.getlist("BenchmarkTest00304")

    if headers:
        param = headers[0]  # just grab first element

    param = param  # URL decoding is not needed in Flask

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == "nt":  # Windows
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:  # Unix/Linux
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "  # Adjust as needed
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))  # execute command
        results = process.read()
        response = results
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response += str(e)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

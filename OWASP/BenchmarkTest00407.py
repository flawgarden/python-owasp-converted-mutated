
import os
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-00/BenchmarkTest00407", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.content_type = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest00407", "")

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[0]

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == "nt":
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')

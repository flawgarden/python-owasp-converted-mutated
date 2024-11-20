
import os
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00575", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = request.response
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00575":
                    param = name
                    flag = False

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Replace with equivalent command if needed

    args_env = {"Foo": "bar"}
    try:
        p = subprocess.Popen(cmd + bar, env=args_env, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        response.data = output.decode() + error.decode()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Escape if necessary
        return response

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

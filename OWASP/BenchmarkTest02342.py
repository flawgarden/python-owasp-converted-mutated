
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02342", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02342":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = subprocess.Popen(cmd + bar, env=args_env, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Use appropriate escaping method if needed.
        return response

    return response

def do_something(param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')

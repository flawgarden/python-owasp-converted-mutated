
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01289", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest01289", "")
    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = subprocess.Popen(cmd + bar, shell=True, env=args_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()

        response.set_data(out.decode())
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
        return response

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[1]  # get the last 'safe' value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

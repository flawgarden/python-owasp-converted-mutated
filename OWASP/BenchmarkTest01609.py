
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01609", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    if request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.values.getlist("BenchmarkTest01609")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == "nt":
        cmd = "echo "  # Adjust for Windows if necessary

    args_env = {"Foo": "bar"}

    try:
        current_dir = os.getcwd()
        process = os.popen(f"{cmd} {bar}", "r")
        output = process.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
        return response

    return response

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

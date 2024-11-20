
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01937", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = app.response_class()
    param = request.headers.get("BenchmarkTest01937", "")

    param = param.encode('utf-8').decode('utf-8')

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)


def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

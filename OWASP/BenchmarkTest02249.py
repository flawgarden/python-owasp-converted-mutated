
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02249", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = ""
    param = request.args.get("BenchmarkTest02249", "")

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "echo "

    try:
        process = os.popen(cmd + bar)
        response = process.read()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response += str(e)

    return response

def do_something(param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

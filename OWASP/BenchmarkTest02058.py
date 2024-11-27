
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02058", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest02058")

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    arg_list = []
    os_name = os.name
    if os_name == 'nt':
        arg_list.append("cmd.exe")
        arg_list.append("/c")
    else:
        arg_list.append("sh")
        arg_list.append("-c")

    arg_list.append("echo " + bar)

    process = os.popen(" ".join(arg_list))

    response = process.read()
    process.close()

    return response

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

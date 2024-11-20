
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02379", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02379", "")
    bar = do_something(param)

    start_uri_slashes = "//" if os.name == 'posix' else "/"

    try:
        file_uri = "file://{}{}{}".format(start_uri_slashes, os.path.abspath("testfiles").replace('\\', os.sep).replace(' ', '_'), bar)
        file_target = os.path.abspath(file_uri)

        response += "Access to file: '{}' created.".format(file_target)
        if os.path.exists(file_target):
            response += " And file already exists."
        else:
            response += " But file doesn't exist yet."
    except Exception as e:
        response += str(e)

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

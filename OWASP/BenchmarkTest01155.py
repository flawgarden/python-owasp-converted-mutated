
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01155", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_data = ""
    param = ""
    if 'BenchmarkTest01155' in request.headers:
        param = request.headers['BenchmarkTest01155']

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    file_target = bar
    response_data += f"Access to file: '{html_escape(file_target)}' created."
    if os.path.exists(file_target):
        response_data += " And file already exists."
    else:
        response_data += " But file doesn't exist yet."

    return response_data

class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[0]  # get the param value

        return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

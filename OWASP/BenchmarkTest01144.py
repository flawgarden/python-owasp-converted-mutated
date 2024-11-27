
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01144", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    for name in request.headers:
        if name in common_headers():
            continue  # If standard header, move on to next one
        param = name  # Grabs the name of the first non-standard header as the parameter
        break

    bar = Test().do_something(request, param)

    # Simulate session attribute setting
    request.environ['werkzeug.server.shutdown']  # Close the session for demonstration
    response.set_data("Item: 'userid' with value: '" + encode_for_html(bar) + "' saved in session.")
    return response

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def common_headers():
    return ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding']

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

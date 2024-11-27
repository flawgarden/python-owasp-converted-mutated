
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/trustbound-01/BenchmarkTest02524", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    values = request.values.getlist("BenchmarkTest02524")
    param = values[0] if values else ""

    bar = do_something(param)

    # Mimicking the session behavior
    request.environ['werkzeug.server.shutdown'] = bar

    response_data = (
        "Item: 'userid' with value: '"
        + encode_for_html(bar)
        + "' saved in session."
    )

    response.set_data(response_data)
    return response

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00711", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.values.getlist("BenchmarkTest00711")
    param = values[0] if values else ""

    bar = ""
    if param:
        valuesList = ["safe", param, "moresafe"]
        valuesList.pop(0)  # remove the 1st safe value
        bar = valuesList[0]  # get the param value

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", bar]
    response.data = f"<!DOCTYPE html>\n<html>\n<body>\n<p>Formatted like: {obj[0]} and {obj[1]}.\n</p>\n</body>\n</html>"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')

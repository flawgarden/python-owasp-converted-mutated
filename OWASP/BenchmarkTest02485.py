
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02485", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest02485")
    param = values[0] if values else ""

    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data("Formatted like: %s and %s." % ("a", bar))
    return response

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = []
        values_list.append("safe")
        values_list.append(param)
        values_list.append("moresafe")

        values_list.pop(0)  # remove the 1st safe value

        bar = values_list[1]  # get the last 'safe' value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

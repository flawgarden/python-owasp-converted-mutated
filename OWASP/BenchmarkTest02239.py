
import os
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02239", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest02239', '')

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
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


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00467", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest00467', '')

    bar = "safe!"
    map88136 = {
        "keyA-88136": "a-Value",  # put some stuff in the collection
        "keyB-88136": param,      # put it in a collection
        "keyC": "another-Value"    # put some stuff in the collection
    }
    bar = map88136.get("keyB-88136")  # get it back out

    response.headers['X-XSS-Protection'] = "0"
    response.data = f"{bar}"

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')

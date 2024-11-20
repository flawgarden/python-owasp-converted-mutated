
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00884", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest00884", '')

    bar = "safe!"
    map26388 = {
        "keyA-26388": "a_Value",
        "keyB-26388": param,
        "keyC": "another_Value"
    }
    bar = map26388.get("keyB-26388")
    bar = map26388.get("keyA-26388")

    response.headers['X-XSS-Protection'] = '0'
    response.data = "Formatted like: {} and {}.".format("a", bar)
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

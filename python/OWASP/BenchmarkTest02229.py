
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02229", methods=['GET', 'POST'])
def benchmark_test_02229():
    if request.method == 'GET':
        return benchmark_test_02229_post()
    return benchmark_test_02229_post()

def benchmark_test_02229_post():
    response = app.response_class()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get('BenchmarkTest02229', '')
    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = f"Formatted like: {'a'} and {bar}."
    return response

def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-26903": "a_Value",
        "keyB-26903": param,
        "keyC": "another_Value"
    }
    bar = map_.get("keyB-26903")
    bar = map_.get("keyA-26903")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

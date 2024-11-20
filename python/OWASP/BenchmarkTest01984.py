
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01984", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    param = ""

    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Language"]:  # Example of common headers
            continue

        param = name
        break

    bar = do_something(request, param)

    file_target = os.path.join('testfiles', bar)
    response.data = f"Access to file: '{file_target}' created."
    
    if os.path.exists(file_target):
        response.data += " And file already exists."
    else:
        response.data += " But file doesn't exist yet."
    
    return response

def do_something(request, param):
    bar = "safe!"
    map_ = {
        "keyA-95438": "a_Value",
        "keyB-95438": param,
        "keyC": "another_Value"
    }
    bar = map_.get("keyB-95438")
    bar = map_.get("keyA-95438")

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

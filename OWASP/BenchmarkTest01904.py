
from flask import Flask, request, Response
import urllib.parse
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01904", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = Response()
        response.headers['Content-Type'] = "text/html;charset=UTF-8"

        param = request.headers.get("BenchmarkTest01904", "")
        param = urllib.parse.unquote(param)

        bar = do_something(request, param)

        file_target = os.path.abspath(bar)
        response.data = f"Access to file: '{file_target}' created.<br>"

        if os.path.exists(file_target):
            response.data += " And file already exists.<br>"
        else:
            response.data += " But file doesn't exist yet.<br>"

        return response

def do_something(request, param):
    bar = "safe!"
    map_ = {
        "keyA-13742": "a-Value",
        "keyB-13742": param,
        "keyC": "another-Value"
    }
    bar = map_["keyB-13742"]
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

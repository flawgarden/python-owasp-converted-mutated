
from flask import Flask, request, send_file
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01158", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest01158")

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    file_name = None
    full_path = None

    try:
        file_name = os.path.join('testfiles', bar)
        full_path = os.path.abspath(file_name)
        return send_file(full_path, as_attachment=False)
    except Exception as e:
        print(f"Couldn't open file: '{full_path}'")
        return "File not found or couldn't be opened!", 404

class Test:
    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)

            bar = values_list[1]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

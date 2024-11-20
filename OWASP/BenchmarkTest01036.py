
import os
from flask import Flask, request, send_file
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01036", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get("BenchmarkTest01036", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    file_name = os.path.join("testfiles", bar)

    try:
        return send_file(file_name, as_attachment=False)
    except Exception as e:
        return f"Couldn't open InputStream on file: '{file_name}'", 500

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map_8487 = {
            "keyA-8487": "a_Value",
            "keyB-8487": param,
            "keyC": "another_Value"
        }
        bar = map_8487.get("keyB-8487")
        bar = map_8487.get("keyA-8487")

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

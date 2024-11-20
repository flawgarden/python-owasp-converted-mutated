
import os
from flask import Flask, request, Response
import pathlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
TESTFILES_DIR = "/path/to/testfiles/"

@app.route("/pathtraver-01/BenchmarkTest01118", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    headers = request.headers
    param = ""

    for name in headers:
        if name in common_headers():
            continue
        
        param = name
        break

    bar = Test().do_something(param)

    file_name = os.path.join(TESTFILES_DIR, bar)
    is_stream = None

    try:
        path = pathlib.Path(file_name)
        is_stream = path.open('rb')
        b = is_stream.read(1000)
        response.set_data(
            "The beginning of file: '{}' is:\n\n{}\n".format(
                escape_html(file_name),
                escape_html(b.decode('utf-8', errors='ignore'))
            )
        )
    except Exception as e:
        response.set_data(
            "Problem getting InputStream: {}".format(escape_html(str(e)))
        )
    finally:
        if is_stream is not None:
            is_stream.close()

    return response

class Test:

    def do_something(self, param):
        bar = "safe!"
        map_ = {
            "keyA-63904": "a_Value",
            "keyB-63904": param,
            "keyC": "another_Value"
        }
        bar = map_["keyB-63904"]
        bar = map_["keyA-63904"]

        return bar

def common_headers():
    return ["Host", "User-Agent", "Accept", "Accept-Encoding", "Connection"]

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

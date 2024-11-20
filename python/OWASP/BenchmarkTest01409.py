
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01409", methods=['GET', 'POST'])
def benchmark_test_01409():
    if request.method == 'GET':
        return benchmark_test_01409_post()

    return benchmark_test_01409_post()

def benchmark_test_01409_post():
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01409":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    file_name = os.path.join('testfiles', bar)
    is_ = None

    try:
        with open(file_name, 'rb') as is_:
            b = is_.read(1000)
            response_text = (
                "The beginning of file: '"
                + escape(file_name)
                + "' is:\n\n" +
                escape(b.decode('utf-8', errors='ignore'))
            )
            return response_text
    except Exception as e:
        print("Couldn't open InputStream on file: '{}'".format(file_name))
        return "Problem getting InputStream: " + escape(str(e))

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-58007": "a_Value",
            "keyB-58007": param,
            "keyC": "another_Value"
        }
        bar = map_["keyB-58007"]
        bar = map_["keyA-58007"]
        return bar

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

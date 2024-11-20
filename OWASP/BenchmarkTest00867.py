
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'path/to/test/files/'

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, key):
        return self.request.args.get(key)

@app.route("/pathtraver-01/BenchmarkTest00867", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00867")

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    file_name = os.path.join(TESTFILES_DIR, bar)
    is_file = None

    try:
        with open(file_name, 'r') as is_file:
            b = is_file.read(1000)
            response.set_data(
                "The beginning of file: '{}' is:\n\n".format(escape(file_name)) +
                escape(b)
            )
    except Exception as e:
        print("Couldn't open InputStream on file: '{}'".format(file_name))
        response.set_data(
            "Problem getting InputStream: {}".format(escape(str(e)))
        )
    return response

def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

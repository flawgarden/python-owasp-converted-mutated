
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'path/to/testfiles/'  # Update with the actual path

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def get_the_parameter(self, param_name):
        return self.request.args.get(param_name, None)

@app.route("/pathtraver-02/BenchmarkTest02382", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    scr = SeparateClassRequest(request)
    param = scr.get_the_parameter("BenchmarkTest02382")
    if param is None:
        param = ""

    bar = do_something(request, param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, bar)

        with open(file_name, 'w') as fos:
            response.set_data("Now ready to write to file: " + file_name)

    except Exception as e:
        print("Couldn't open FileOutputStream on file: '" + str(file_name) + "'")

    return response

def do_something(request, param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

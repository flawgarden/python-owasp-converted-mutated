
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles/'  # Set the directory for test files

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name, '')

@app.route("/pathtraver-03/BenchmarkTest02667", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest02667")

    bar = do_something(param)

    file_name = os.path.join(TESTFILES_DIR, bar)

    try:
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response.data = f"The beginning of file: '{escape(file_name)}' is:\n\n"
            response.data += escape(b.decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
    
    return response

def do_something(param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "your_testfiles_directory/"  # Specify your test files directory

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, key):
        return self.request.args.get(key) or self.request.form.get(key)

@app.route("/pathtraver-03/BenchmarkTest02669", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest02669")

    bar = do_something(param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, bar)

        fos = open(file_name, 'w')
        return f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    finally:
        if fos is not None:
            try:
                fos.close()
                fos = None
            except Exception as e:
                pass

def do_something(param):
    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

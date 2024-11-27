
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01572", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_text = ""
    values = request.form.getlist("BenchmarkTest01572")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join('path/to/test/files', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_text += "The beginning of file: '{}' is:\n\n{}".format(
                escape(file_name), escape(b.decode('utf-8', errors='ignore')))
    except Exception as e:
        print("Couldn't open FileInputStream on file: '{}'".format(file_name))
        response_text += "Problem getting FileInputStream: {}".format(escape(str(e)))
    
    return response_text

class Test:

    def do_something(self, param):
        # Simulating ThingFactory and ThingInterface functionality
        return param  # Replace this with actual logic

def escape(string):
    # Basic HTML escaping function
    return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

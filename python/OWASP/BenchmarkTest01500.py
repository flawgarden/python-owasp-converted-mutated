
import os
from flask import Flask, request, render_template, send_file

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01500", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.values.get("BenchmarkTest01500", "")
    
    bar = Test().do_something(param)
    
    file_name = os.path.join('testfiles', bar)
    
    try:
        with open(file_name, 'rb') as file:
            b = file.read(1000)
            response += ("The beginning of file: '" + escape(file_name) + "' is:\n\n")
            response += escape(b.decode('utf-8'))
    except Exception as e:
        print(f"Couldn't open InputStream on file: '{file_name}'")
        response += ("Problem getting InputStream: " + escape(str(e)))

    return response

class Test:

    def do_something(self, param):
        bar = "safe!"
        map_ = {
            "keyA-3545": "a-Value",
            "keyB-3545": param,
            "keyC": "another-Value"
        }
        bar = map_.get("keyB-3545")
        return bar

def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

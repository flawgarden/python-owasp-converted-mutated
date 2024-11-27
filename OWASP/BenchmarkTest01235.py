
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01235", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.form.get("BenchmarkTest01235", "")
        bar = Test().do_something(request, param)

        start_uri_slashes = ""
        if os.name == "nt":
            start_uri_slashes = "/"
        else:
            start_uri_slashes = "//"

        try:
            file_uri = f"file:{start_uri_slashes}{os.path.abspath('testfiles').replace(os.sep, '/').replace(' ', '_')}{bar}"
            file_target = os.path.normpath(file_uri)

            output = f"Access to file: '{file_target}' created."
            
            if os.path.exists(file_target):
                output += " And file already exists."
            else:
                output += " But file doesn't exist yet."
                
            return output
        except Exception as e:
            raise Exception(e)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_13886 = {
            "keyA-13886": "a-Value",
            "keyB-13886": param,
            "keyC": "another-Value"
        }
        bar = map_13886["keyB-13886"]
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

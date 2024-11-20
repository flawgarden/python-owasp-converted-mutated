
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01752", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest01752", "")

    bar = Test().do_something(request, param)

    file_name = os.path.join("testfiles/", bar)

    try:
        with open(file_name, 'a') as fos:
            return f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
        return "Error"

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_11351 = {
            "keyA-11351": "a-Value",
            "keyB-11351": param,
            "keyC": "another-Value"
        }
        bar = map_11351.get("keyB-11351")
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01231", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01231", "")
    bar = Test().do_something(request, param)

    file_target = os.path.join('path/to/testfiles_dir', bar)
    response_text = "Access to file: '{}' created.".format(file_target)

    if os.path.exists(file_target):
        response_text += " And file already exists."
    else:
        response_text += " But file doesn't exist yet."

    return render_template("response.html", response=response_text)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map35717 = {}
        map35717["keyA-35717"] = "a-Value"
        map35717["keyB-35717"] = param
        map35717["keyC"] = "another-Value"
        bar = map35717["keyB-35717"]

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

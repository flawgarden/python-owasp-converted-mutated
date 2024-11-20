
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00359", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return render_template("index.html")

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00359", "")
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    file_target = os.path.abspath(bar)
    output = "Access to file: '{} created.".format(file_target)

    if os.path.exists(file_target):
        output += " And file already exists."
    else:
        output += " But file doesn't exist yet."

    return output

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

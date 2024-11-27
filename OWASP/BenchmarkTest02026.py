
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02026", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = ""
    headers = request.headers.get("BenchmarkTest02026")

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    file_target = os.path.join(os.getcwd(), "testfiles", bar)  # Adjust to appropriate path
    output = "Access to file: '" + file_target + "' created."

    if os.path.exists(file_target):
        output += " And file already exists."
    else:
        output += " But file doesn't exist yet."

    return output

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value

        bar = values_list[1]  # get the last 'safe' value

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

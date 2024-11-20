
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02204", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    map = request.args
    param = ""
    if map:
        values = map.getlist("BenchmarkTest02204")
        if values:
            param = values[0]

    bar = do_something(param)
    file_name = os.path.join("test_files", bar)

    try:
        with open(file_name, 'wb') as f:
            response += "Now ready to write to file: " + file_name
    except Exception as e:
        print("Couldn't open FileOutputStream on file: '" + file_name + "'")

    return response

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

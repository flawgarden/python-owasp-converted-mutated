
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02468", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_html = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest02468")
    param = values[0] if values else ""

    bar = do_something(param)

    file_name = os.path.join('testfiles', bar)

    try:
        with open(file_name, 'w') as fos:
            return f"Now ready to write to file: {html_escape(file_name)}"
    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

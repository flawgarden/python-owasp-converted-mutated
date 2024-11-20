
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02301", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        if flag:
            values = request.args.getlist(name)
            if values:
                for value in values:
                    if value == "BenchmarkTest02301":
                        param = name
                        flag = False

    bar = do_something(param)

    file_target = bar
    response_message = "Access to file: '" + file_target + "' created."

    if os.path.exists(file_target):
        response_message += " And file already exists."
    else:
        response_message += " But file doesn't exist yet."

    return render_template("index.html", message=response_message)

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)

        bar = values_list[1]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00864", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.values.get("BenchmarkTest00864", None)
    bar = "alsosafe"

    if param is not None:
        valuesList = ["safe", param, "moresafe"]
        valuesList.pop(0)  # remove the 1st safe value
        bar = valuesList[1]  # get the last 'safe' value

    fileTarget = os.path.join(bar, "Test.txt")
    response_message = (
        "Access to file: '"
        + fileTarget
        + "' created."
    )
    if os.path.exists(fileTarget):
        response_message += " And file already exists."
    else:
        response_message += " But file doesn't exist yet."

    return response_message

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

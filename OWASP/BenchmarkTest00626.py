
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00626", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = request.form.get("BenchmarkTest00626", "")

    bar = "alsosafe"
    if param is not None:
        valuesList = ["safe", param, "moresafe"]
        valuesList.pop(0)  # remove the 1st safe value
        bar = valuesList[1]  # get the last 'safe' value

    fileName = None
    fos = None

    try:
        fileName = os.path.join('testfiles', bar)

        with open(fileName, 'w') as fos:
            response.data = f"Now ready to write to file: {fileName}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{fileName}'")

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

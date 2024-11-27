
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00865", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"

    param = request.args.get('BenchmarkTest00865', None)

    bar = ""
    if param is not None:
        valuesList = []
        valuesList.append("safe")
        valuesList.append(param)
        valuesList.append("moresafe")

        valuesList.pop(0)  # remove the 1st safe value

        bar = valuesList[0]  # get the param value

    startURIslashes = ""
    if os.name == 'nt':
        startURIslashes = "/"
    else:
        startURIslashes = "//"

    try:
        fileURI = urllib.parse.urljoin("file:", startURIslashes + os.path.normpath("TESTFILES_DIR").replace('\\', os.path.sep).replace(' ', '_') + bar)
        fileTarget = os.path.normpath(fileURI)
        response_text = f"Access to file: '{fileTarget}' created.<br>"
        if os.path.exists(fileTarget):
            response_text += "And file already exists.<br>"
        else:
            response_text += "But file doesn't exist yet.<br>"
        return response_text
    except Exception as e:
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

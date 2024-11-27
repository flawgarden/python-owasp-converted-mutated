
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00528", methods=['GET', 'POST'])
def benchmark_test_00528():
    if request.method == 'GET':
        return benchmark_test_00528_post()
    return benchmark_test_00528_post()

def benchmark_test_00528_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00528":
                    param = name
                    flag = False
                    break

    bar = "safe!"
    map6751 = {
        "keyA-6751": "a-Value",
        "keyB-6751": param,
        "keyC": "another-Value"
    }
    bar = map6751["keyB-6751"]

    start_uri_slashes = ""
    if os.name == "nt":
        start_uri_slashes = "/"
    else:
        start_uri_slashes = "//"

    try:
        file_uri = urllib.parse.urljoin(
            "file:",
            start_uri_slashes + os.path.abspath('TESTFILES_DIR').replace('\\', os.path.sep).replace(' ', '_') + bar
        )
        file_target = urllib.parse.urlparse(file_uri).path
        
        response_text = f"Access to file: '{file_target}' created."
        
        if os.path.exists(file_target):
            response_text += " And file already exists."
        else:
            response_text += " But file doesn't exist yet."

        return render_template("index.html", response=response_text)

    except Exception as e:
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

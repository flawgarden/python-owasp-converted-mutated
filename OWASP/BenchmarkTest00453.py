
import os
import base64
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/pathtraver-00/BenchmarkTest00453", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    
    param = request.args.get("BenchmarkTest00453", "")
    
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    startURIslashes = "//" if os.name != 'nt' else "/"

    try:
        file_uri = f"file:{startURIslashes}{os.path.normpath('testfiles').replace(' ', '_')}{bar}"
        file_target = os.path.abspath(file_uri)

        response.data = (
            f"Access to file: '{file_target}' created.<br>"
        )
        if os.path.exists(file_target):
            response.data += " And file already exists."
        else:
            response.data += " But file doesn't exist yet."
    except Exception as e:
        return str(e), 500

    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

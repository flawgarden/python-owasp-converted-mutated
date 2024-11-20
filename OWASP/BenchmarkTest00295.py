
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00295", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    if 'BenchmarkTest00295' in request.headers:
        param = request.headers['BenchmarkTest00295']

    param = urllib.parse.unquote(param)

    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    os_name = os.name
    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
    else:
        a1 = "sh"
        a2 = "-c"

    args = [a1, a2, "echo " + bar]

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        return output
    except IOError as e:
        print("Problem executing cmdi - subprocess issue")
        return str(e), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

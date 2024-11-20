
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01030", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("BenchmarkTest01030") is not None:
        param = request.headers.get("BenchmarkTest01030")

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    start_uri_slashes = "//" if os.name == 'posix' else "/"

    try:
        file_uri = f"file:{start_uri_slashes}{os.path.normpath('testfiles').replace(' ', '_')}/{bar}"
        file_target = os.path.abspath(file_uri)

        response_content = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            response_content += " And file already exists."
        else:
            response_content += " But file doesn't exist yet."

        return render_template("response.html", response_content=response_content)

    except Exception as e:
        return str(e)

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

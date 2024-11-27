
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02034", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.getlist("BenchmarkTest02034")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    file_name = 'testfiles/' + bar

    try:
        with open(file_name, 'wb') as fos:
            response.data = f"Now ready to write to file: {file_name}".encode('utf-8')

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    return response

def do_something(request, param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

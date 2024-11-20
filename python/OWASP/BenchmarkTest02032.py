
from flask import Flask, request, Response
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02032", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = ""
        headers = request.headers.getlist("BenchmarkTest02032")

        if headers:
            param = headers[0]  # just grab first element

        param = urllib.parse.unquote(param)

        bar = do_something(param)

        file_name = None
        try:
            file_name = os.path.join("path_to_test_files_directory", bar)  # adjust path accordingly
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                response.data = (
                    f"The beginning of file: '{escape(file_name)}' is:\n\n" +
                    escape(b.decode('utf-8', errors='ignore'))
                )
        except Exception as e:
            print(f"Couldn't open FileInputStream on file: '{file_name}'")
        
        return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

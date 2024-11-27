
import os
from flask import Flask, request, render_template, send_file
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02562", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest02562="
    param_loc = query_string.find(paramval)

    response_html = ""

    if param_loc == -1:
        response_html += f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string."
        return response_html

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    file_name = None

    try:
        file_name = os.path.join('path/to/testfiles', bar)  # Change this path accordingly.
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_html += f"The beginning of file: '{file_name}' is:\n\n"
            response_html += b.decode("utf-8", errors='ignore')
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")

    return response_html

def do_something(param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

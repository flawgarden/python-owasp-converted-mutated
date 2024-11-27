
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01646", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01646="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.set_data(
            f"getQueryString() couldn't find expected parameter 'BenchmarkTest01646' in query string.")
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    file_name = None
    try:
        file_name = f"uploads/{bar}"

        with open(file_name, 'w') as fos:
            response.set_data(
                f"Now ready to write to file: {file_name}")

    except Exception as e:
        print(f"Couldn't open file output stream on file: '{file_name}'")

    return response

class Test:

    def do_something(self, param):
        bar = "safe!"
        map84260 = {}
        map84260["keyA-84260"] = "a_Value"
        map84260["keyB-84260"] = param
        map84260["keyC"] = "another_Value"
        bar = map84260["keyB-84260"]
        bar = map84260["keyA-84260"]

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

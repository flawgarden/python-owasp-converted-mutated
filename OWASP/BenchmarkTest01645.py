
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01645", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01645="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01645' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    file_name = None
    try:
        file_name = f"YOUR_TEST_FILES_DIR/{bar}"
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            content = f"The beginning of file: '{file_name}' is:\n\n"
            content += urllib.parse.quote_plus(b.decode('utf-8'))
            return content
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
    return "File not found."

class Test:
    def do_something(self, request, param):
        bar = None
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

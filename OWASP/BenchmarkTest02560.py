
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02560", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = {}
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02560="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response['message'] = f"getQueryString() couldn't find expected parameter '{paramval}'."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param

    bar = do_something(request, param)

    file_name = None
    try:
        file_name = os.path.join("testfiles_dir", bar)  # Assuming 'testfiles_dir' is defined
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response['file_content'] = f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
    except Exception as e:
        response['message'] = f"Problem getting File: {str(e)}"

    return response

def do_something(request, param):
    bar = param
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

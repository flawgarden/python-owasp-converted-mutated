
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-03/BenchmarkTest02559", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    else:
        return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02559="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02559' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    start_urislashes = "//" if os.name == 'posix' else "/"

    try:
        file_uri = f"file:{start_urislashes}{os.path.join('path_to_test_files_dir', bar).replace(' ', '_')}"
        file_target = os.path.normpath(file_uri)
        response_message = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            response_message += " And file already exists."
        else:
            response_message += " But file doesn't exist yet."
        return response_message
    except Exception as e:
        return str(e)

def do_something(request, param):
    return param  # Placeholder for the actual implementation

if __name__ == "__main__":
    app.run(host='0.0.0.0')

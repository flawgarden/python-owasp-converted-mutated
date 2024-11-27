
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02567", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02567" + "="
    param_loc = -1

    if query_string:
        param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02567' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param.replace("%20", " ")  # Simple URL decode

    bar = do_something(request, param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join('testfiles', bar)

        with open(file_name, 'w') as fos:
            response += f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    return response

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-03/BenchmarkTest02570", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02570="
    paramLoc = query_string.find(paramval)

    if paramLoc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02570' in query string."

    param = query_string[paramLoc + len(paramval):]
    ampersandLoc = query_string.find("&", paramLoc)
    if ampersandLoc != -1:
        param = query_string[paramLoc + len(paramval):ampersandLoc]
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    file_name = os.path.join("path_to_testfiles", bar)
    try:
        with open(file_name, 'rb') as is_:
            b = is_.read(1000)
            response_content = f"The beginning of file: '{file_name}' is:\n\n"
            response_content += str(b.decode('utf-8', 'ignore'))
            return Response(response_content, content_type='text/html;charset=UTF-8')
    except Exception as e:
        return f"Couldn't open InputStream on file: '{file_name}'. Problem getting InputStream: {str(e)}"

def do_something(request, param):
    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

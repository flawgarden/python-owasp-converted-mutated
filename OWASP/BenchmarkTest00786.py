
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00786", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00786="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = "safe!"
    map29957 = {
        "keyA-29957": "a_Value",
        "keyB-29957": param,
        "keyC": "another_Value"
    }
    bar = map29957["keyB-29957"]
    bar = map29957["keyA-29957"]

    file_name = None
    try:
        file_name = os.path.join("testfiles", bar)
        with open(file_name, "w") as fos:
            response.data = f"Now ready to write to file: {urllib.parse.quote(file_name)}"
    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

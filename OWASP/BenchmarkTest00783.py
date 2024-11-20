
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00783", methods=['GET', 'POST'])
def benchmark_test_00783():
    if request.method == 'GET':
        return benchmark_test_00783_post()

    return benchmark_test_00783_post()

def benchmark_test_00783_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00783="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00783' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map_2299 = {
        "keyA-2299": "a-Value",
        "keyB-2299": param,
        "keyC": "another-Value"
    }
    bar = map_2299["keyB-2299"]

    file_name = os.path.join("testfiles", bar)

    try:
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return f"Problem getting file: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
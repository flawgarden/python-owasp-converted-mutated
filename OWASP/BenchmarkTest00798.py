
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest00798", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = ""
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00798="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00798' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + "Z"

    try:
        algorithm = "SHA5"  # Default algorithm, could be made dynamic if required
        md = hashlib.new(algorithm)
        input_data = bar.encode() if isinstance(bar, str) else bar

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response += "Sensitive value '{}' hashed and stored<br/>".format(input_data.decode())

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    response += "Hash Test hashlib.new('{}') executed".format(algorithm)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

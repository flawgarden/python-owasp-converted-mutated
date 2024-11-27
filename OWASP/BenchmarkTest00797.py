
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00797", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""

    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00797="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00797' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + 'Z'

    try:
        # Load properties (dummy implementation, can be replaced with real loading)
        algorithm = 'sha512'  # For now we are using SHA512 directly
        md = hashlib.new(algorithm)
        input_param = bar.encode()
        md.update(input_param)
        result = md.digest()

        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response += f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    response += "Hash Test executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

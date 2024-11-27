
import os
import hashlib
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01656", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01656="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01656' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    try:
        algorithm = "SHA5"  # Default, adjust based on your configuration
        md = hashlib.new(algorithm)
        input_data = bytearray(b'?')
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        return str(e)

class Test:

    def do_something(self, param):
        bar = ""
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

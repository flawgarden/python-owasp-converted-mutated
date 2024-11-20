
import os
import urllib.parse
from flask import Flask, request, Response, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01653", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = Response()
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01653="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter 'BenchmarkTest01653' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        md = hashlib.md5()
        input_bytes = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_bytes = input_param.encode()
        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join("path/to/test/files/", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")  # Assuming you want hex representation
            
        response.data = f"Sensitive value '{input_bytes.decode()}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase", str(e))
        response.data = str(e)
    
    response.data += "Hash Test hashlib.md5() executed"
    return response

class Test:
    def do_something(self, request, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

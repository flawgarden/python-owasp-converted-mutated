
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01651", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode()
    param_val = "BenchmarkTest01651="
    param_loc = query_string.find(param_val)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01651' in query string."

    param = query_string[param_loc + len(param_val):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(param_val):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)
    result = hash_value(bar)

    return f"Sensitive value '{escape_html(param)}' hashed and stored<br/>Hash Test executed"

def hash_value(bar):
    hash_object = hashlib.sha1()
    input_value = bar.encode('utf-8')
    hash_object.update(input_value)
    result = hash_object.digest()

    file_target = os.path.join("testfiles", "passwordFile.txt")
    with open(file_target, "a") as fw:
        fw.write("hash_value=" + str(result.hex()) + "\n")

    return result

def escape_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

class Test:
    def do_something(self, request, param):
        return escape_html(param)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

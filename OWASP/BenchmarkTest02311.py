
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02311", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        for value in values:
            if value == "BenchmarkTest02311":
                param = name
                flag = False
                break
        if not flag:
            break

    bar = do_something(param)

    try:
        md = hashlib.md5()
        input_bytes = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_bytes = input_param.encode()

        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(
            escape_html(input_bytes.decode('utf-8'))
        )

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        bar = param[:-1]
    return bar

def escape_html(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import hashlib
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00266", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = ""
    headers = request.headers.getlist("BenchmarkTest00266")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map42712 = {
        "keyA-42712": "a-Value",
        "keyB-42712": param,
        "keyC": "another-Value"
    }

    bar = map42712["keyB-42712"]

    try:
        if len(hashlib.algorithms_available) > 1:
            md = hashlib.new("sha1")
        else:
            md = hashlib.new("sha1")
        input_param = bar.encode()  # Assuming bar is always a string
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join("uploads", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")  # Storing hashed value as hexadecimal

        return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>", response

    except Exception as e:
        print("Problem executing hash")
        return str(e), response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

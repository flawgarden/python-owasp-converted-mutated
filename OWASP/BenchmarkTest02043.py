
import os
import urllib.parse
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest02043", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.getlist("BenchmarkTest02043")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    try:
        algorithm = "SHA5"
        md = hashlib.new(algorithm)

        input_data = b'?'  # default input
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + result + b"\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

def do_something(param):
    bar = "safe!"
    map52182 = {
        "keyA-52182": "a_Value",
        "keyB-52182": param,
        "keyC": "another_Value"
    }
    bar = map52182.get("keyB-52182")  # get it back out
    bar = map52182.get("keyA-52182")  # get safe value back out
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import urllib.parse
import hashlib
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest01041", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01041", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    try:
        algorithm = "SHA512"
        hasher = hashlib.new(algorithm)
        input_data = bytearray(b'?')
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()

        hasher.update(input_data)

        result = hasher.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import hashlib
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00142", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00142", "")
    param = urllib.parse.unquote(param)

    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    try:
        md = hashlib.sha256()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path_to_your_directory", "passwordFile.txt")
        with open(file_target, "ab") as fw:
            fw.write(b"hash_value=" + result + b"\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return "An error occurred", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')

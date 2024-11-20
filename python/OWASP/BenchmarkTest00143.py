
import os
import urllib.parse
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00143", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = request.headers.get("BenchmarkTest00143", "")
    param = urllib.parse.unquote(param)

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

    try:
        algorithm = "SHA512"

        md = hashlib.new(algorithm)
        input_data = b'?'  # default input

        if isinstance(bar, str):
            input_data = bar.encode()
        elif isinstance(bar, bytes):
            input_data = bar

        md.update(input_data)
        result = md.digest()

        file_target = os.path.join(os.getcwd(), "passwordFile.txt")
        with open(file_target, "ab") as fw:
            fw.write(f"hash_value={result.hex()}\n".encode())

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

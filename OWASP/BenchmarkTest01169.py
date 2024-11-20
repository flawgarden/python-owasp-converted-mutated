
import os
import hashlib
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest01169", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"

    param = ""
    headers = request.headers.get("BenchmarkTest01169")

    if headers:
        param = headers  # just grab first element

    # URL Decode the header value
    param = unquote(param)

    bar = Test().do_something(request, param)

    try:
        algorithm = "SHA5"  # Default algorithm, replace with appropriate loading mechanism if needed
        md = hashlib.new(algorithm)  # Create a new hash object
        input_data = b'?'
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path_to_your_testfiles_dir", "passwordFile.txt")

        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")  # Storing as hex for simplicity

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>", response_content

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

class Test:

    def do_something(self, request, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

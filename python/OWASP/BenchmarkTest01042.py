
import os
import io
import base64
from flask import Flask, request, render_template
import hashlib
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-01/BenchmarkTest01042", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01042", "")
    param = unquote(param)

    bar = Test().do_something(param)

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_data = (b'?')
        input_param = bar
        
        if isinstance(input_param, str):
            input_data = input_param.encode()
        elif isinstance(input_param, io.BytesIO):
            str_input = input_param.read(1000)
            if not str_input:
                return "This input source requires a POST, not a GET. Incompatible UI for the InputStream source."
            input_data = str_input
            
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return f"Sensitive value '{html_encode(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e


class Test:

    def do_something(self, param):
        return f"{param}_SafeStuff"


def html_encode(text):
    return "".join(f"&#{ord(c)};" for c in text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00229", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers.keys():
        if name in common_headers():
            continue  # If standard header, move on to next one

        param = name
        break

    bar = escape_html(param)

    try:
        algorithm = "SHA5"  # Default algorithm
        hash_object = hashlib.new(algorithm)
        input_data = bar.encode('utf-8')

        hash_object.update(input_data)
        result = hash_object.digest()

        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={base64.b64encode(result).decode('utf-8')}\n")

        return f"Sensitive value '{escape_html(input_data.decode('utf-8'))}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

def common_headers():
    return {'Content-Type', 'User-Agent'}

def escape_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

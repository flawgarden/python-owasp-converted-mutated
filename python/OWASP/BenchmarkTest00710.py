
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00710", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.form.getlist("BenchmarkTest00710")
    param = values[0] if values else ""

    bar = param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)

        input_data = bar.encode('utf-8')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/your/directory", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        response += "Sensitive value '" + bar + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

    response += "Hash Test hashlib.new(algorithm) executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

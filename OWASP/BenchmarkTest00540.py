
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00540", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.to_dict() if request.method == 'GET' else request.form.to_dict()
    for name in names:
        values = request.form.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00540":
                    param = name
                    flag = False
                    break

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        benchmarkprops = {}
        with open('benchmark.properties') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    benchmarkprops[key] = value.strip()

        algorithm = benchmarkprops.get("hashAlg2", "SHA5")
        if algorithm == "SHA5":
            algorithm = "sha256"  # SHA5 is not a standard algorithm; using sha256 as an example

        input_data = b'?'  # Default input
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()
        elif isinstance(input_param, bytes):
            input_data = input_param

        # Hashing
        md = hashlib.new(algorithm)
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:  # 'a' for append
            fw.write("hash_value=" + result.hex() + "\n")

        response_data = f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

    return response_data + "Hash Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

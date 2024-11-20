
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00640", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest00640", "")
    bar = ""

    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        with open("benchmark.properties") as f:
            benchmarkprops = dict(line.strip().split('=') for line in f if line and not line.startswith('#'))
        algorithm = benchmarkprops.get("hashAlg2", "SHA5")

        if algorithm not in hashlib.algorithms_available:
            algorithm = "sha256"

        md = hashlib.new(algorithm)
        input_param = bar.encode('utf-8')

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")
        
        with open(file_target, "a") as fw:
            fw.write(f"hash_value={result.hex()}\n")

        return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

if __name__ == "__main__":
    app.run(host='0.0.0.0')

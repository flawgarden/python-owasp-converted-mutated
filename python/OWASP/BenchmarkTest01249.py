
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01249", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01249", "")
    bar = Test().do_something(param)

    try:
        algorithm = os.getenv("hashAlg2", "SHA5")
        md = hashlib.new(algorithm, b'?' if bar is None else bar.encode())

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        return f"Sensitive value '{bar}' hashed and stored<br/>"
    
    except ValueError as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

class Test:
    def do_something(self, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

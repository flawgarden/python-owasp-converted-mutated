
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles'  # Set to your desired directory for test files

@app.route("/hash-00/BenchmarkTest00225", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Encoding", "Content-Type"]:  # example common headers
            continue
        
        param = name
        break

    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    try:
        m = hashlib.new('sha512')
        input_value = bar.encode() if isinstance(bar, str) else bar
        m.update(input_value)

        result = m.digest()
        file_target = os.path.join(TESTFILES_DIR, "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")  # Store in hex format for simplicity
            
        return f"Sensitive value '{input_value.decode()}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash", str(e))
        return "Error processing hash"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

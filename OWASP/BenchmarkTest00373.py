
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00373", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00373", "")
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    try:
        sha256 = hashlib.sha256()
        input_data = b'?'

        if isinstance(bar, str):
            input_data = bar.encode()

        sha256.update(input_data)

        result = sha256.digest()
        file_target = os.path.join('path/to/directory/', 'passwordFile.txt')  # Update with actual path to store file

        with open(file_target, 'a') as fw:  # the 'a' mode will append the new data
            fw.write("hash_value=" + result.hex() + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(input_data.decode())

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import hashlib
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest00876", methods=['GET', 'POST'])
def benchmark_test_00876():
    if request.method == 'GET':
        return benchmark_test_00876_post(request)

    return benchmark_test_00876_post(request)

def benchmark_test_00876_post(request):
    param = request.args.get("BenchmarkTest00876", "")

    bar = ""

    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_param = bar.encode()

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join("uploads", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response_message = f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"
        return response_message

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

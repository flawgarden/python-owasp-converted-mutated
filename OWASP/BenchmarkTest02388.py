
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-02/BenchmarkTest02388", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.values.get("BenchmarkTest02388", "")
    bar = do_something(request, param)

    try:
        md = hashlib.md5()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.getcwd(), "passwordFile.txt")
        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + result + b"\n")

        response_message = f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

    response_message += "Hash Test hashlib.md5() executed"
    return response_message


def do_something(request, param):
    bar = "safe!"
    map94322 = {
        "keyA-94322": "a_Value",
        "keyB-94322": param,
        "keyC": "another_Value"
    }
    bar = map94322["keyB-94322"]
    bar = map94322["keyA-94322"]

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

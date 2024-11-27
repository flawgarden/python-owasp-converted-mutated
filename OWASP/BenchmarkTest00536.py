
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00536", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args

    for name in names:
        values = request.form.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00536":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = "safe!"
    map28714 = {}
    map28714["keyA-28714"] = "a-Value"
    map28714["keyB-28714"] = param
    map28714["keyC"] = "another-Value"
    bar = map28714["keyB-28714"]

    try:
        md = hashlib.md5()
        input = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input = input_param.encode()
        md.update(input)

        result = md.digest()
        file_target = os.path.join("path_to_your_directory", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')

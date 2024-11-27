
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest01416", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True

    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01416":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_data = b'?'
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path_to_your_directory', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(input_data.decode())

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

class Test:
    def do_something(self, param):
        bar = ""

        # Simple if statement that assigns param to bar on true condition
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

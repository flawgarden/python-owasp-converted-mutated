
import os
import base64
import hashlib
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01164", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")
    param = request.headers.get('BenchmarkTest01164', '')

    param = base64.urlsafe_b64decode(param).decode('utf-8')

    bar = Test().do_something(param)

    try:
        if len(hashlib.algorithms_available) > 1:
            md = hashlib.new("sha384", usedforsecurity=False)
        else:
            md = hashlib.new("sha384")

        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        elif isinstance(input_param, bytes):
            input_data = input_param

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.path.dirname(__file__), "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response.data += "Sensitive value '{}' hashed and stored<br/>".format(
            base64.b64encode(input_data).decode('utf-8'))

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new")
        raise e

    response.data += "Hash Test hashlib.new executed"

    return response


class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')

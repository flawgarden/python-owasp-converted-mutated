
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest01414", methods=['GET', 'POST'])
def benchmark_test_01414():
    if request.method == 'GET':
        return benchmark_test_01414_post()

    return benchmark_test_01414_post()

def benchmark_test_01414_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01414":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    try:
        algorithm = 'sha512'
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md = hashlib.new(algorithm)
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('uploads/', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

class Test:

    def do_something(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

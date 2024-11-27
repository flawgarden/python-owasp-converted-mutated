
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest02391", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02391", "")
    bar = do_something(param)

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_data = b'?'
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path_to_your_testfiles_dir", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return "Sensitive value '" + input_data.decode() + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

def do_something(param):
    # Simulate whatever the doSomething function was intended to do
    return param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

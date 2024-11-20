
from flask import Flask, request, render_template
import hashlib
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01766", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.form.get("BenchmarkTest01766", "")

    bar = do_something(param)

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        elif isinstance(input_param, bytes):
            input_data = input_param

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        response += "Sensitive value '" + encode_for_html(input_data.decode()) + "' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response += "Hash Test hashlib.new(algorithm) executed"
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]
    return bar

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    return data.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

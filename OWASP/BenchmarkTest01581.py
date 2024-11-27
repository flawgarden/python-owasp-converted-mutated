
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01581", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    values = request.values.getlist("BenchmarkTest01581")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    try:
        algorithm = "SHA5"  # Adjust as needed
        md = hashlib.new(algorithm)
        input_data = b'?'
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()
        elif isinstance(input_param, bytes):
            input_data = input_param

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        return f"Sensitive value '{encode_for_html(input_data.decode())}' hashed and stored<br/>"

    except ValueError as e:
        raise Exception("Problem executing hash - TestCase") from e

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    from html import escape
    return escape(data)

class Test:

    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

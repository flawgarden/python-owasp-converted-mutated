
from flask import Flask, request, render_template
import os
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-02/BenchmarkTest02678", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    response = {}
    response['content_type'] = 'text/html;charset=UTF-8'
    return response


def benchmark_test_post():
    response = {}
    response['content_type'] = 'text/html;charset=UTF-8'

    param = request.values.get("BenchmarkTest02678", None)

    bar = do_something(param)

    try:
        algorithm = "SHA5"  # Change to appropriate hashing algorithm if needed
        if algorithm == "SHA5":
            md = hashlib.new("sha5")
        else:
            md = hashlib.new(algorithm)

        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()
        elif isinstance(bar, bytes):
            input_data = bar

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")
        
        with open(file_target, 'a') as fw:  # the 'a' will append the new data
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")
        
        response['message'] = ("Sensitive value '{}' hashed and stored<br/>".format(
            escape_html(input_data.decode())
        ))

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response['message'] += "Hash Test executed"
    return response


def do_something(param):
    bar = ""
    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar


def escape_html(string):
    # Basic HTML escaping
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

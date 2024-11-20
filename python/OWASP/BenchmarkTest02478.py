
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02478", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest02478")
    param = values[0] if values else ""

    bar = do_something(param)

    try:
        algorithm = "SHA512"
        if 'hashAlg1' in app.config:
            algorithm = app.config['hashAlg1']
        import hashlib
        md = hashlib.new(algorithm)
        input_bytes = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_bytes = input_param.encode()
        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        response += ("Sensitive value '" + escape_for_html(input_bytes.decode()) + "' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash - TestCase")
        response += str(e)

    response += "Hash Test executed"
    return response

def do_something(param):
    bar = ""
    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def escape_for_html(value):
    from html import escape
    return escape(value)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

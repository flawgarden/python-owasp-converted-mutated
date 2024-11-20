
import os
import sys
from flask import Flask, request, render_template, make_response
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02044", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():

    param = ""
    headers = request.headers.get('BenchmarkTest02044')

    if headers:
        param = headers  # just grab the first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    try:
        algorithm = "SHA5"  # or retrieve from properties as in Java code
        hasher = hashlib.new(algorithm)
        input_data = b'?'  # byte representation of the input

        if isinstance(bar, str):
            input_data = bar.encode()

        hasher.update(input_data)

        result = hasher.digest()
        file_target = os.path.join("path_to_testfiles_dir", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        response = make_response(
            "Sensitive value '" + encode_for_html(input_data.decode()) + "' hashed and stored<br/>"
        )
        return response

    except Exception as e:
        print("Problem executing hash - TestCase", file=sys.stderr)
        return str(e)

def do_something(param):
    return param + "_SafeStuff"

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    import html
    return html.escape(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

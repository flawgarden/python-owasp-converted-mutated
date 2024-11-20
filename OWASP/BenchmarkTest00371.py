
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00371", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.form.get("BenchmarkTest00371", "")

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    try:
        input_data = bar.encode() if isinstance(bar, str) else bytearray(b'?')

        hash_object = hashlib.new("sha1")
        hash_object.update(input_data)
        result = hash_object.digest()

        file_target = os.path.join('test_files', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        return "Sensitive value '" + escape_html(input_data.decode()) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha1')")
        raise e

def escape_html(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02479", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    values = request.values.getlist("BenchmarkTest02479")
    param = values[0] if values else ""

    bar = do_something(param)

    try:
        algorithm = "SHA5"  # Set default algorithm
        benchmarkprops_path = os.path.join(os.path.dirname(__file__), 'benchmark.properties')
        if os.path.exists(benchmarkprops_path):
            with open(benchmarkprops_path) as f:
                for line in f:
                    if line.startswith("hashAlg2"):
                        algorithm = line.split("=")[1].strip()

        md = hashlib.new(algorithm)
        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join(os.path.dirname(__file__), 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += "Sensitive value '" + escape_html(input_param.decode('utf-8')) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise Exception(e)

    response += "Hash Test executed"
    return response

def do_something(param):
    bar = escape_html(param)
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

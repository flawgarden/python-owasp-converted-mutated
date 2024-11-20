
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02392", methods=['GET', 'POST'])
def benchmark_test_02392():
    if request.method == 'GET':
        return benchmark_test_02392_post(request)

    return benchmark_test_02392_post(request)

def benchmark_test_02392_post(request):
    response = ""
    benchmarkprops = {"hashAlg1": "SHA512"}
    algorithm = benchmarkprops.get("hashAlg1", "SHA512")

    param = request.args.get("BenchmarkTest02392", "")
    bar = do_something(request, param)

    input_data = b'?'
    if isinstance(bar, str):
        input_data = bar.encode()

    try:
        md = hashlib.new(algorithm)
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += "Sensitive value '" + escape_html(input_data.decode('utf-8')) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    response += "Hash Test hashlib.new(algorithm) executed"
    return response

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[1]
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

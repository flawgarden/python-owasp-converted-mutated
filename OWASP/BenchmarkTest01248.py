
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01248", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = ""
    param = request.args.get('BenchmarkTest01248', '')

    bar = Test().do_something(request, param)

    try:
        algorithm = "SHA512"  # You can load from a properties file if needed
        md = hashlib.new(algorithm)

        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("TESTFILES_DIR", "passwordFile.txt")

        with open(file_target, "a") as fw:
            fw.write(f"hash_value={base64.b64encode(result).decode()}\\n")

        response += f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    response += "Hash Test executed"
    return response

def html_escape(text):
    escape_table = {
        "&": "&amp;",
        ">": "&gt;",
        "<": "&lt;",
        '"': "&quot;",
        "'": "&#x27;"
    }
    return ''.join(escape_table.get(c, c) for c in text)

class Test:

    @staticmethod
    def do_something(request, param):
        bar = param
        if param is not None and len(param) > 1:
            bar = param[:-1]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

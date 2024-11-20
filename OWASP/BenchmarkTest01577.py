
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01577", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    values = request.values.getlist("BenchmarkTest01577")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    try:
        md = hashlib.md5()
        input_data = b'?'  # Default input
        if isinstance(bar, str):
            input_data = bar.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path_to_testfiles_dir', 'passwordFile.txt')

        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + base64.b64encode(result) + b"\n")

        response_message = f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

    return response_message + "Hash Test hashlib.md5 executed"

class Test:

    def do_something(self, param):
        return html_escape(param)

def html_escape(text):
    """Escape HTML special characters"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

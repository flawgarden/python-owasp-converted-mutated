
import os
import base64
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02121", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.form.get("BenchmarkTest02121", "")
    bar = do_something(param)

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)

        if isinstance(bar, str):
            input_data = bar.encode()
        else:
            input_data = bytearray(b'?')

        md.update(input_data)
        result = md.digest()

        file_target = os.path.join("path_to_your_test_files", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        return f"Sensitive value '{escape_html(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

def escape_html(s):
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&#039;"))

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

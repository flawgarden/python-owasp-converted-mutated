
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00870", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"
    param = request.form.get("BenchmarkTest00870", None)

    if param is not None:
        bar = escape_html(param)

        try:
            md = hashlib.new('sha1')
            input_data = b'?'
            if isinstance(bar, str):
                input_data = bar.encode()
            md.update(input_data)

            result = md.digest()
            file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
            with open(file_target, "a") as fw:
                fw.write("hash_value=" + encode_base64(result) + "\n")

            return f"Sensitive value '{escape_html(input_data.decode())}' hashed and stored<br/>"
        except Exception as e:
            print("Problem executing hash")
            return str(e)

    return "Hash Test executed"

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def encode_base64(input_bytes):
    return base64.b64encode(input_bytes).decode()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

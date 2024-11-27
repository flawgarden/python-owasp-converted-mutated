
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'path_to_testfiles_dir'  # Set the appropriate path

@app.route("/hash-00/BenchmarkTest00224", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post()
    if request.method == 'POST':
        return do_post()

def do_post():
    param = ""
    for name in request.headers:
        if name in common_headers():  # Replace with actual header names to skip
            continue

        param = name
        break

    bar = param

    try:
        md = hashlib.new('sha384')

        input_data = bar.encode('utf-8') if isinstance(bar, str) else bytearray(b'?')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(TESTFILES_DIR, "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        return f"Sensitive value '{encode_for_html(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        return str(e)

def common_headers():
    return ['User-Agent', 'Accept']  # Example of headers to skip

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode('utf-8')

def encode_for_html(data):
    import html
    return html.escape(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

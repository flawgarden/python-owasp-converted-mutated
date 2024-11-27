
import os
import hashlib
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route("/hash-02/BenchmarkTest02210", methods=['GET', 'POST'])
def benchmark_test_02210():
    if request.method == 'GET':
        return benchmark_test_02210_post()

    return benchmark_test_02210_post()

def benchmark_test_02210_post():
    map = request.values
    param = ""
    if map:
        values = map.getlist("BenchmarkTest02210")
        if values:
            param = values[0]

    bar = do_something(param)

    try:
        md = hashlib.new('sha384')
        input_data = bar.encode('utf-8') if isinstance(bar, str) else bar
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('uploads/', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return jsonify({
            'message': f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored"
        })

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha384')")
        return jsonify({'error': str(e)}), 500

def do_something(param):
    return html_escape(param)

def html_escape(text):
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;"))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

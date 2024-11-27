
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02387", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02387', "")
    bar = do_something(param)

    try:
        md5_hash = hashlib.md5()
        input_data = bytes('?','utf-8')

        if isinstance(bar, str):
            input_data = bar.encode('utf-8')

        md5_hash.update(input_data)
        result = md5_hash.digest()

        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return f"Sensitive value '{html_escape(bar)}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

def do_something(param):
    bar = "safe!"
    map = {
        "keyA-70399": "a-Value",
        "keyB-70399": param,
        "keyC": "another-Value"
    }
    bar = map["keyB-70399"]
    return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

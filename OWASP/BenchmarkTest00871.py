
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00871", methods=['GET', 'POST'])
def benchmark_test_00871():
    if request.method == 'GET':
        return benchmark_test_00871_post()

    return "This endpoint only supports GET and POST methods."

def benchmark_test_00871_post():
    param = request.args.get("BenchmarkTest00871", "")
    bar = "safe!"
    
    map42157 = {
        "keyA-42157": "a-Value",
        "keyB-42157": param,
        "keyC": "another-Value"
    }
    
    bar = map42157["keyB-42157"]

    try:
        input_data = bar.encode() if isinstance(bar, str) else b'?'
        
        sha1 = hashlib.new('sha1')  # Using SHA1 hashing algorithm
        sha1.update(input_data)

        result = sha1.digest()
        file_target = os.path.join("path/to/your/directory", "passwordFile.txt")
        
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={base64.b64encode(result).decode()}\n")

        return (
            f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"
            "Hash Test executed successfully."
        )

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

def html_escape(text):
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

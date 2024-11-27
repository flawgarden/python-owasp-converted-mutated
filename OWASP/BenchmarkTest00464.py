
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00464", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00464", "")

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    try:
        md = hashlib.new('sha1')
        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return render_template("index.html", message=f"Sensitive value '{escape_input(input_data.decode())}' hashed and stored<br/>")
    
    except Exception as e:
        return render_template("index.html", message="An error occurred during hashing.")

def escape_input(input_str):
    return input_str.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;").replace("\"", "&quot;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

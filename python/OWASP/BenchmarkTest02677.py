
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest02677", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02677', default='', type=str)
    bar = do_something(param)
    
    try:
        algorithm = 'SHA512'
        md = hashlib.new(algorithm)
        input_data = b'?' if bar is None else bar.encode('utf-8')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")
        
        return f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        bar = param[:-1] + 'Z'
    return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01993", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    headers = request.headers
    param = ""

    for name in headers:
        if name not in common_headers():
            param = name
            break

    bar = do_something(param)

    import hashlib
    sha384 = hashlib.sha384()
    input_param = bar.encode('utf-8') if isinstance(bar, str) else bar

    sha384.update(input_param)

    result = sha384.digest()
    file_target = os.path.join('path_to_test_files/', 'passwordFile.txt')

    with open(file_target, 'a') as fw:
        fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

    return f"Sensitive value '{html_encode(input_param.decode())}' hashed and stored<br/>"

def common_headers():
    return {'Content-Type', 'User-Agent', 'Accept', 'Accept-Language'}

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode('utf-8')))
    return bar

def html_encode(input_str):
    return input_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

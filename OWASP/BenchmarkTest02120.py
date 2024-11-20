
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02120", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02120")
    if param is None:
        param = ""

    bar = do_something(param)

    try:
        import hashlib
        md = hashlib.sha256()

        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        return f"Sensitive value '{escape_html(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

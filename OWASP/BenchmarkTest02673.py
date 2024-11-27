
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02673", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest02673")

    bar = do_something(param)

    try:
        if len(hashlib.algorithms_available) > 1:
            md = hashlib.new("sha384")
        else:
            md = hashlib.sha384()

        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/test/files", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")
        
        response += ("Sensitive value '" + escape_html(str(input_data)) + "' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash")
        raise

    response += "Hash Test executed"
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + 'Z'
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

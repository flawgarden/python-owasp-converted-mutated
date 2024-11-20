
import os
from flask import Flask, request, render_template
import hashlib
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02041", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    
    param = ""
    headers = request.headers.get("BenchmarkTest02041")

    if headers:
        param = headers # grab first element

    param = unquote(param)

    bar = do_something(request, param)

    try:
        md = hashlib.new("sha384")

        input_data = b'?'  
        input_param = bar.encode() if isinstance(bar, str) else bar

        if isinstance(input_param, bytes):
            input_data = input_param
        else:
            response = "This input source requires a POST, not a GET. Incompatible UI for the InputStream source."
            return response

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path_to_your_testfiles_dir", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response = "Sensitive value '{} hashed and stored<br/>".format(input_data.decode('utf-8'))

    except Exception as e:
        print("Problem executing hash - TestCase.")
        return str(e)

    response += "Hash Test executed"
    return response

def do_something(request, param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

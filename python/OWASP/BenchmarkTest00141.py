
import os
import urllib.parse
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00141", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00141", "")
    param = urllib.parse.unquote(param)

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        md = hashlib.new('sha1')
        input_param = bar.encode() if isinstance(bar, str) else bar

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join(os.getcwd(), "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode("utf-8") + "\n")
        
        return f"Sensitive value '{html_escape(input_param.decode())}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash")
        raise Exception(e)

def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

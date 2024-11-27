
import os
import hashlib
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00268", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    if request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response_content = "<html><body>"
    param = ""
    headers = request.headers.getlist("BenchmarkTest00268")

    if headers:
        param = headers[0]  # just grab first element

    # URL Decode the header value
    param = unquote(param)

    bar = ""

    # Simple ? condition that assigns param to bar on false condition
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        # Hashing the input with SHA1
        md = hashlib.sha1()
        if isinstance(bar, str):
            input_data = bar.encode()
        else:
            input_data = bytes(bar)

        md.update(input_data)

        # Getting result of hashing
        result = md.digest()
        file_target = os.path.join("your_path_here", "passwordFile.txt")
        with open(file_target, "ab") as fw:
            fw.write(b"hash_value=" + result + b"\n")

        response_content += f"Sensitive value '{html_encode(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha1")
        response_content += str(e)

    response_content += "Hash Test executed</body></html>"
    return response_content

def html_encode(data):
    # Simple HTML encoder for the output
    return data.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

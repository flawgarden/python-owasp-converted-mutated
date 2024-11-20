
import os
from flask import Flask, request, render_template, jsonify
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00227", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = ""
    param = ""
    for name in request.headers:
        if name in ['Content-Type', 'User-Agent', 'Accept']:  # Replace with common headers you want to ignore
            continue
        param = name  # Grabs the name of the first non-standard header as the parameter
        break

    # Chain a bunch of propagators in sequence
    a15913 = param
    b15913 = a15913 + " SafeStuff"
    b15913 = b15913[:-5] + "Chars"  # replace some of the end content
    map15913 = {"key15913": b15913}
    c15913 = map15913["key15913"]
    d15913 = c15913[:-1]  # extract most of it
    e15913 = base64.b64decode(base64.b64encode(d15913.encode())).decode()  # B64 encode and decode it
    f15913 = e15913.split(" ")[0]  # split it on a space

    thing = create_thing()  # Define this function as needed
    g15913 = "barbarians_at_the_gate"  # This is static so this whole flow is 'safe'
    bar = thing.do_something(g15913)  # reflection

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_bytes = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_bytes = input_param.encode()
        elif isinstance(input_param, bytes):
            input_bytes = input_param
        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        response_content = "Sensitive value '" + escape_html(str(input_bytes)) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return jsonify({"error": str(e)}), 500

    return response_content + "Hash Test executed"

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class Thing:
    def do_something(self, g15913):
        return "dummy_output"  # Replace with actual behavior

def create_thing():
    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

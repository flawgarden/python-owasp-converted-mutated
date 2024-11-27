
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01995", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = ""

    for name in request.headers:
        if name in common_headers:
            continue
        param = name
        break

    bar = do_something(request, param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()

        md.update(input_data)
        result = md.digest()

        file_target = os.path.join(TESTFILES_DIR, "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        response += f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    response += "Hash Test hashlib.sha256 executed"
    return response

def do_something(request, param):
    a33633 = param
    b33633 = a33633 + " SafeStuff"
    b33633 = b33633[:-1] + "Chars"
    map33633 = {'key33633': b33633}
    c33633 = map33633['key33633']
    d33633 = c33633[:-1]
    e33633 = base64.b64decode(base64.b64encode(d33633.encode())).decode()
    f33633 = e33633.split(" ")[0]

    thing = create_thing()
    g33633 = "barbarians_at_the_gate"
    bar = thing.do_something(g33633)

    return bar

common_headers = ["Content-Type", "User-Agent", "Accept", "Host"]
TESTFILES_DIR = "path/to/testfiles"

class ThingInterface:
    def do_something(self, input):
        # Logic for doing something
        return input

def create_thing():
    return ThingInterface()

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01994", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = ""

    param = ""
    for name in request.headers:
        if name in common_headers:
            continue

        param = name
        break

    bar = do_something(request, param)

    try:
        md = hashlib.new('sha384')
        input_data = bar.encode('utf-8')

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/your/test/files", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += f"Sensitive value '{escape_html(input_data.decode('utf-8'))}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        raise e

    response += "Hash Test executed"
    return response

def do_something(request, param):
    thing = create_thing()
    bar = thing.do_something(param)
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    return Thing()

class Thing:
    def do_something(self, input):
        return input

common_headers = ["Content-Type", "User-Agent", "Accept"]

if __name__ == "__main__":
    app.run(host='0.0.0.0')

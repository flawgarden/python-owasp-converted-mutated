
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01576", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest01576")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    try:
        md = hashlib.sha512()
        input = b'?'  # Default byte
        if isinstance(bar, str):
            input = bar.encode()
        md.update(input)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            encoded_result = result.hex()  # Using hex for a simple representation
            fw.write(f"hash_value={encoded_result}\n")

        response_message = f"Sensitive value '{html_escape(input.decode())}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    return response_message + "Hash Test executed"

class Test:
    def do_something(self, request, param):
        bar = param
        return bar

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

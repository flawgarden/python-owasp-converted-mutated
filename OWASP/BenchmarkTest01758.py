
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-01/BenchmarkTest01758", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.values.get("BenchmarkTest01758", "")

    bar = Test().do_something(param)

    try:
        md = hashlib.new('sha384')

        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()
        elif isinstance(bar, bytes):
            input_data = bar

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'ab') as fw:  # Append mode
            fw.write(b"hash_value=" + base64.b64encode(result) + b"\n")

        return f"Sensitive value '{html_encode(input_data.decode())}' hashed and stored<br/>" + \
               "Hash Test executed"

    except Exception as e:
        print("Problem executing hash")
        raise

class Test:

    def do_something(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar


def html_encode(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

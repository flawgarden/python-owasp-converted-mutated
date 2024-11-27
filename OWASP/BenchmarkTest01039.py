
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01039", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01039", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        md = hashlib.sha256()
        input_param = bar.encode('utf-8')

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        return f"Sensitive value '{encode_for_html(input_param.decode())}' hashed and stored<br/>" \
               f"Hash Test hashlib.sha256() executed"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 106

        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

        return bar

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    from html import escape
    return escape(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01757", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""

    param = request.form.get("BenchmarkTest01757")

    bar = Test().do_something(param)

    try:
        import hashlib
        md = hashlib.new('sha1')

        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'ab') as fw:
            fw.write(
                b"hash_value=" + base64.b64encode(result) + b"\n"
            )
        response += "Sensitive value '" + escape_html(input_param.decode('utf-8')) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash:", e)
        raise

    response += "Hash Test executed"
    return response

class Test:

    def do_something(self, param):
        bar = ""
        if param is not None:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

def escape_html(text):
    from html import escape
    return escape(text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

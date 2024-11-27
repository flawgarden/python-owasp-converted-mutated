
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02215", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    map = request.form
    param = ""
    if map:
        values = map.getlist("BenchmarkTest02215")
        if values:
            param = values[0]

    bar = do_something(param)

    try:
        m = hashlib.new('sha512')
        input_param = bar.encode() if isinstance(bar, str) else bar
        m.update(input_param)

        result = m.digest()
        file_path = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_path, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        response += "Sensitive value '" + encode_for_html(input_param.decode()) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha512')")
        return str(e)

    response += "Hash Test hashlib.new('sha512') executed"
    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode('utf-8')

def encode_for_html(data):
    import html
    return html.escape(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

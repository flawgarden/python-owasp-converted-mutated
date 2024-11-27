
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02672", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02672", default=None)
    bar = do_something(param)

    try:
        md = hashlib.new("sha384")
        input_data = bytes(bar, 'utf-8')

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("TESTFILES_DIR", "passwordFile.txt")
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(html_escape(input_data.decode('utf-8')))

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

def do_something(param):
    bar = "safe!"
    map_ = {'keyA-48519': "a_Value", 'keyB-48519': param, 'keyC': "another_Value"}
    bar = map_.get('keyB-48519')
    bar = map_.get('keyA-48519')
    return bar

def html_escape(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#x27;"))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

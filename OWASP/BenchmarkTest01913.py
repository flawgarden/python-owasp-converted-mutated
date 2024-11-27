
import os
import urllib.parse
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01913", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = ""
    param = request.headers.get("BenchmarkTest01913", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("TESTFILES_DIR", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        response_content += "Sensitive value '" + input_data.decode() + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

    response_content += "Hash Test hashlib.sha256() executed"
    return response_content

def do_something(param):
    thing = create_thing()
    bar = thing.do_something(param)
    return bar

def create_thing():
    return Thing()

class Thing:
    def do_something(self, param):
        # Mock implementation for demonstration purposes
        return param[::-1]

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

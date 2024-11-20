
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01167", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest01167")

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        md = hashlib.md5()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('uploads', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_70586 = {}
        map_70586["keyA-70586"] = "a-Value"
        map_70586["keyB-70586"] = param
        map_70586["keyC"] = "another-Value"
        bar = map_70586["keyB-70586"]

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

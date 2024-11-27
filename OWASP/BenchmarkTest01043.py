
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest01043", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get("BenchmarkTest01043", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_value = bar.encode('utf-8')
        md.update(input_value)

        result = md.digest()

        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(urllib.parse.quote_plus(str(input_value)))

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

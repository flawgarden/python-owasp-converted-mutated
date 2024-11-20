
import os
import hashlib
from flask import Flask, request, render_template
from html import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01244", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01244", "")
    bar = Test().do_something(param)

    try:
        md = hashlib.new('sha1')

        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{escape(bar)}' hashed and stored<br/>" + \
               "Hash Test executed"

    except Exception as e:
        print(f"Problem executing hash - {e}")
        return "Error occurred during hashing"

class Test:

    def do_something(self, param):
        bar = escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

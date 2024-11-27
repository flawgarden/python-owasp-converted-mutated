
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01332", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest01332', '')

    bar = Test().do_something(param)

    try:
        md = hashlib.new("sha512")
        input_data = bar.encode() if isinstance(bar, str) else bar

        md.update(input_data)

        result = md.digest()

        file_target = os.path.join('path_to_your_testfiles_directory', 'passwordFile.txt')
        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + result + b"\n")

        response += f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new()")
        raise Exception(e)

    response += "Hash Test hashlib.new() executed"
    return response

class Test:

    def do_something(self, param):
        sbxyz43527 = str(param)
        bar = sbxyz43527 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

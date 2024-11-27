
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00372", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00372", "")
    bar = ""

    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        md = hashlib.md5()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

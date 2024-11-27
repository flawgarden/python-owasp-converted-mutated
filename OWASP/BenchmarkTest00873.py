
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00873", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = request.form.get("BenchmarkTest00873")

    bar = "safe!"
    map58847 = {
        "keyA-58847": "a_Value",
        "keyB-58847": param,
        "keyC": "another_Value"
    }
    bar = map58847.get("keyB-58847")
    bar = map58847.get("keyA-58847")

    try:
        input_param = bar.encode('utf-8') if isinstance(bar, str) else bar
        md = hashlib.new('sha512')
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        encoded_input = base64.b64encode(input_param).decode('utf-8')
        response = f"Sensitive value '{encoded_input}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha512')")
        raise e

    return response + "Hash Test hashlib.new('sha512') executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

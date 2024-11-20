
import os
from flask import Flask, request, render_template
import hashlib
from werkzeug.utils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-01/BenchmarkTest00874", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest00874", "")
    bar = escape(param)

    try:
        # SHA-512 Hashing
        md = hashlib.sha512()
        input_param = bar.encode() if isinstance(bar, str) else bar

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response = f"Sensitive value '{escape(input_param.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha512()")
        response = str(e)

    return response + "Hash Test hashlib.sha512() executed"


if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00703", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    values = request.form.getlist("BenchmarkTest00703")
    param = values[0] if values else ""

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[0]

    result = None
    try:
        if isinstance(bar, str):
            input_data = bar.encode()
        else:
            # Handle other types if necessary
            input_data = b'?'

        md = hashlib.sha1()
        md.update(input_data)
        result = md.digest()

        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return render_template("index.html", message=f"Sensitive value '{input_data.decode()}' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha1()")
        raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')

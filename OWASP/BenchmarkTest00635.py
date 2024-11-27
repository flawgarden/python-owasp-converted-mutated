
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00635", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get("BenchmarkTest00635", "")
    bar = escape(param)

    try:
        md = hashlib.new('sha1')
        input_param = bar.encode('utf-8')
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('path_to_testfiles_directory', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return f"Sensitive value '{escape(input_param.decode('utf-8'))}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        raise

def escape(value):
    return value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

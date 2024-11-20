
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02308", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02308":
                    param = name
                    flag = False
                    break
    
    bar = do_something(param)

    try:
        md = hashlib.new("sha1")
        input_param = bar
        if isinstance(input_param, str):
            input_bytes = input_param.encode()
        else:
            input_bytes = bytes([ord('?')])

        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join('tests', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        return render_template("index.html", message=f"Sensitive value '{input_param}' hashed and stored<br/>")

    except Exception as e:
        raise Exception("Problem executing hash") from e

def do_something(param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template, Response
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02476", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = Response()
        values = request.values.getlist("BenchmarkTest02476")
        param = values[0] if values else ""

        bar = do_something(request, param)

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
                fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

            response.data = (
                "Sensitive value '"
                + base64.b64encode(input_data).decode()
                + "' hashed and stored<br/>"
            )

        except Exception as e:
            raise Exception("Problem executing hash - TestCase") from e

        response.data += "Hash Test executed"
        return response
    return render_template("index.html")

def do_something(request, param):
    bar = ""
    if param:
        bar = param.split(" ")[0]
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00706", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest00706")
    param = values[0] if values else ""

    bar = param  # For simplicity, assuming no additional encoding is done here

    try:
        md = hashlib.new("sha512")
        input_data = b'?'
        input_param = bar.encode('utf-8')

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += "<br/>Sensitive value '" + input_param.decode('utf-8') + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

    response += "Hash Test executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

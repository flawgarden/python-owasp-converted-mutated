
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00709", methods=['GET', 'POST'])
def benchmark_test_00709():
    if request.method == 'GET':
        return benchmark_test_00709_post()

    return benchmark_test_00709_post()

def benchmark_test_00709_post():
    response = Flask.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest00709")
    param = values[0] if values else ""

    bar = param  # Replace with appropriate encoding if needed

    try:
        md = hashlib.sha256()
        input_bytes = bar.encode() if isinstance(bar, str) else bar
        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join('path_to_testfiles_dir', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response.set_data(f"Sensitive value '{input_bytes.decode()}' hashed and stored<br/>")
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

    response.set_data(response.get_data(as_text=True) +
                      "Hash Test executed")
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00537", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_html = ""
    param = ""
    flag = True

    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00537":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = param

    try:
        md = hashlib.md5()
        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode('utf-8')

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response_html += "Sensitive value '" + secure_filename(bar) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response_html += "Hash Test executed"
    return response_html

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

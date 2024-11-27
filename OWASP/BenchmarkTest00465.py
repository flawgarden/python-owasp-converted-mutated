
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "path/to/test/files/"  # Set the correct path to the test files directory

@app.route("/hash-00/BenchmarkTest00465", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post()
    return do_post()

def do_post():
    response = "text/html;charset=UTF-8"
    param = request.args.get('BenchmarkTest00465', '')

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    try:
        md = hashlib.md5()
        input_data = bar.encode() if isinstance(bar, str) else bytes('?', 'utf-8')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(TESTFILES_DIR, "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={result.hex()}\n")  # Writing the hex digest

        return (f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"
                f"Hash Test hashlib.md5() executed")
    
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

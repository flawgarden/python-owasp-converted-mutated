
import os
import hashlib
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/hash-02/BenchmarkTest02675", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = ""
        param = request.form.get("BenchmarkTest02675")
        bar = do_something(param)

        try:
            md = hashlib.md5()
            input_data = bar.encode() if isinstance(bar, str) else bar
            md.update(input_data)

            result = md.digest()
            file_target = os.path.join(app.config['UPLOAD_FOLDER'], 'passwordFile.txt')
            with open(file_target, 'a') as fw:
                fw.write("hash_value=" + str(result.hex()) + "\n")
            
            response += "Sensitive value '{}' hashed and stored<br/>".format(input_data.decode())

        except Exception as e:
            print("Problem executing hash - TestCase")
            return "Error: {}".format(str(e))

        response += "Hash Test executed"
        return response

    return render_template("index.html")

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        bar = param[:-1]
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

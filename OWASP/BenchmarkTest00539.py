
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/hash-00/BenchmarkTest00539", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post()

    return do_post()

def do_post():
    param = ""
    flag = True
    names = request.args if request.method == 'GET' else request.form
    for name in names:
        values = names.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00539":
                    param = name
                    flag = False

    bar = ""
    if param:
        bar = param.split(" ")[0]

    try:
        md = hashlib.sha256()
        input_data = b'?'  # default input

        if isinstance(bar, str):
            input_data = bar.encode()
        
        md.update(input_data)

        result = md.digest()
        
        file_target = os.path.join(UPLOAD_FOLDER, "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={result.hex()}\n")
        
        return render_template("index.html", message=f"Sensitive value '{input_data.decode()}' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

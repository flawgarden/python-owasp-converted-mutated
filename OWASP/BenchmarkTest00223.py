
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00223", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection']:  # common headers
            continue
        param = name  # Grab the name of the first non-standard header as the parameter
        break

    bar = "safe!"
    map_ = {
        "keyA-13848": "a-Value",  # put some stuff in the collection
        "keyB-13848": param,      # put it in a collection
        "keyC": "another-Value"    # put some stuff in the collection
    }
    bar = map_["keyB-13848"]  # get it back out

    try:
        input_data = bar.encode('utf-8')
        md = hashlib.new('sha1')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path_to_your_testfiles_directory", "passwordFile.txt")
        with open(file_target, "a") as fw:  # the true will append the new data
            fw.write(f"hash_value={base64.b64encode(result).decode('utf-8')}\n")
        
        return f"Sensitive value '{input_data.decode('utf-8')}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase java.security.MessageDigest.getInstance(java.lang.String,java.security.Provider)")
        raise RuntimeError(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

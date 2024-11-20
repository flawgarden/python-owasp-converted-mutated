
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/hash-00/BenchmarkTest00531", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    if request.method == 'POST':
        return benchmark_test_post()


def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()  # Changed to request.args for GET request
    for name in names:
        values = request.args.getlist(name)  # Changed to getlist to get all values
        if values:
            for value in values:
                if value == "BenchmarkTest00531":
                    param = name
                    flag = False
                    break

    bar = "safe!"
    map_38098 = {
        "keyA-38098": "a-Value",  # put some stuff in the collection
        "keyB-38098": param,  # put it in a collection
        "keyC": "another-Value"  # put some stuff in the collection
    }
    bar = map_38098.get("keyB-38098")  # get it back out

    hash_input = bar.encode() if isinstance(bar, str) else bar
    md = hashlib.new("sha1")  # Create a sha1 hash object
    md.update(hash_input)

    result = md.digest()
    file_target = os.path.join(os.path.dirname(__file__), "passwordFile.txt")
    with open(file_target, "a") as fw:
        fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

    return "Sensitive value '{}' hashed and stored<br/>".format(request.args.get('value', ''))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

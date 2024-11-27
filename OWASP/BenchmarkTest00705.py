
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00705", methods=['GET', 'POST'])
def benchmark_test_00705():
    if request.method == 'GET':
        return benchmark_test_00705_post()
    return benchmark_test_00705_post()

def benchmark_test_00705_post():
    response = ""
    response += "<html><body>"
    values = request.form.getlist("BenchmarkTest00705")
    param = values[0] if values else ""

    bar = "safe!"
    map_ = {
        "keyA-71551": "a_Value",
        "keyB-71551": param,
        "keyC": "another_Value"
    }
    bar = map_["keyB-71551"]
    bar = map_["keyA-71551"]

    try:
        md = hashlib.new('sha1')
        input_data = b'?'  # default input

        if isinstance(bar, str):
            input_data = bar.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response += "Sensitive value '" + input_data.decode() + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new()")
        response += "Error occurred: " + str(e)

    response += "Hash Test hashlib.new() executed"
    response += "</body></html>"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

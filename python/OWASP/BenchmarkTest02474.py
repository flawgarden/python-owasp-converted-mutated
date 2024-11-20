
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02474", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = ""
    values = request.values.getlist("BenchmarkTest02474")
    param = values[0] if values else ""

    bar = do_something(param)

    try:
        hash_object = hashlib.sha1()
        input_data = bar.encode() if isinstance(bar, str) else bar
        hash_object.update(input_data)

        result = hash_object.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")
        
        response += f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha1()")
        raise Exception(e)

    response += "Hash Test hashlib.sha1() executed"
    return response

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

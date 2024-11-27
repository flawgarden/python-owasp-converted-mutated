
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00228", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name in common_headers():
            continue
        param = name
        break

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[0]

    try:
        algorithm = "SHA5"  # Default algorithm
        properties = load_benchmark_properties()
        if 'hashAlg2' in properties:
            algorithm = properties['hashAlg2']

        md = hashlib.new(algorithm)
        input_data = b'?'  # Default input byte
        if isinstance(bar, str):
            input_data = bar.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_base64(result) + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(encode_html(input_data))

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

def load_benchmark_properties():
    properties = {}
    with open('benchmark.properties') as f:
        for line in f:
            key, value = line.strip().split('=')
            properties[key] = value
    return properties

def common_headers():
    return ['Accept', 'User-Agent', 'Content-Type']

def encode_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_html(data):
    return data.decode().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

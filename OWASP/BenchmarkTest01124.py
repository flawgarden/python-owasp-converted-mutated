
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01124", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    param = ""

    for name in request.headers:
        if name in common_headers():
            continue
        
        param = name
        break

    bar = Test().do_something(request, param)
    
    try:
        algorithm = "SHA512"  # Default algorithm
        md = hashlib.new(algorithm)
        input_data = b'?'
        
        if isinstance(bar, str):
            input_data = bar.encode()
        elif isinstance(bar, bytes):
            input_data = bar
        
        md.update(input_data)
        result = md.digest()
        
        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")
        
        response.data = f"Sensitive value '{encode_for_html(input_data.decode())}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response.data += "Hash Test executed"
    return response

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map_74702 = {}
        map_74702["keyA-74702"] = "a_Value"
        map_74702["keyB-74702"] = param
        map_74702["keyC"] = "another_Value"
        bar = map_74702["keyB-74702"]
        bar = map_74702["keyA-74702"]
        return bar

def common_headers():
    return ["Host", "User-Agent", "Accept", "Accept-Language", "Connection"]

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    from html import escape
    return escape(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import hashlib
from flask import Flask, request, render_template
import urllib.parse
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00790", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)

    return do_post(request)

def do_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00790="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00790' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = escape(param)

    try:
        md = hashlib.new('sha1')
        input_data = bytearray(b'?')
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.getcwd(), "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        return f"Sensitive value '{escape(str(input_data))}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        raise e

    return "Hash Test executed"

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def encode_for_base64(data):
    return base64.b64encode(data).decode('utf-8')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

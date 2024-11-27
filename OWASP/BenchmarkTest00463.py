
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00463", methods=['GET', 'POST'])
def benchmark_test_00463():
    if request.method == 'GET':
        return do_post(request)
    return do_post(request)

def do_post(request):
    response = ""
    param = request.args.get("BenchmarkTest00463", "")

    bar = escape_html(param)
    
    try:
        md = hashlib.new('sha384')
        input_data = bar.encode('utf-8')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.path.dirname(__file__), "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + encode_base64(result) + "\n")

        response += f"Sensitive value '{escape_html(input_data.decode())}' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash.")
        return str(e)
    
    response += "Hash Test executed"
    return response

def escape_html(data):
    return data.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def encode_base64(data):
    return base64.b64encode(data).decode('utf-8')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

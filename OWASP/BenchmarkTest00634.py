
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00634", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)

    return do_post(request)

def do_post(request):
    response = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest00634", "")
    bar = ""

    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[0]

    try:
        md = hashlib.new("sha1")
        input_param = bar.encode() if isinstance(bar, str) else bar
        input_data = input_param if isinstance(input_param, bytes) else b'?'  
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        response += f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        response += f"Error: {str(e)}"

    response += "Hash Test executed"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')


import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00632", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)

    return do_post(request)

def do_post(request):
    response = "text/html;charset=UTF-8"
    param = request.args.get('BenchmarkTest00632', '')
    
    bar = ""
    if param:
        bar = param.split(" ")[0]

    try:
        # SHA-384 hashing
        if bar:
            input_data = bar.encode()
        else:
            input_data = bytes('?', 'utf-8')
        
        hashed = hashlib.sha384(input_data).digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + str(hashed.hex()) + "\n")
        
        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print(f"Problem executing hash - {str(e)}")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

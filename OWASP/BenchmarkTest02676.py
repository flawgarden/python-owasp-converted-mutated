
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02676", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02676', '')

    bar = do_something(param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        
        with open(file_target, 'a') as fw:  # the 'a' will append the new data
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")
        
        response_message = "Sensitive value '" + base64.b64encode(input_data).decode('utf-8') + "' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    return response_message + "Hash Test executed"

def do_something(param):
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    else:
        bar = ''
    
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

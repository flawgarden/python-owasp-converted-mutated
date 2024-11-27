
from flask import Flask, request, render_template
import os
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00046", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_values = []
    response_values.append("Content-Type: text/html;charset=UTF-8")
    
    if 'BenchmarkTest00046' in request.form:
        param = request.form['BenchmarkTest00046']
    else:
        param = ""

    try:
        md = hashlib.md5()
        input_data = bytes('?', 'utf-8')

        if isinstance(param, str):
            input_data = param.encode()
        
        md.update(input_data)

        result = md.digest()
        
        file_target = os.path.join('uploads/', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")
        
        response_values.append("Sensitive value '" + escape(input_data.decode()) + "' hashed and stored<br/>")
        
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)
    
    response_values.append("Hash Test hashlib.md5 executed")
    return ''.join(response_values)

def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

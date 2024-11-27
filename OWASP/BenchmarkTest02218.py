
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02218", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = request.args.get('BenchmarkTest02218', '')

    bar = do_something(param)
    
    try:
        md = hashlib.sha256()
        input_param = bar.encode() if isinstance(bar, str) else bar
        
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        
        with open(file_target, 'a') as fw:  # the 'a' will append the new data
            fw.write("hash_value=" + encode_for_base64(result) + "\n")

        return "Sensitive value '" + encode_for_html(input_param.decode()) + "' hashed and stored<br/>"
        
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

def do_something(param):
    bar = encode_for_html(param)
    return bar

def encode_for_base64(data):
    import base64
    return base64.b64encode(data).decode()

def encode_for_html(data):
    from html import escape
    return escape(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

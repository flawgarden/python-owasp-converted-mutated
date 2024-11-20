
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest02211", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_helper(request)
    return benchmark_test_helper(request)

def benchmark_test_helper(request):
    param = request.args.get('BenchmarkTest02211', '')
    bar = do_something(param)

    try:
        md = hashlib.new('sha1')
        input_param = bar.encode('utf-8')
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles/', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{bar}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha1')")
        raise e

def do_something(param):
    bar = escape(param)  # Assuming escape is a function similar to ESAPI.encoder().encodeForHTML
    return bar

def escape(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

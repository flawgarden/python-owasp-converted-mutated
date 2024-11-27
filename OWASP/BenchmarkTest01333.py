
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-01/BenchmarkTest01333", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get('BenchmarkTest01333', '')

    bar = Test().do_something(param)

    try:
        md = hashlib.md5()
        input_data = bar.encode('utf-8')

        md.update(input_data)
        result = md.digest()

        file_target = os.path.join("testfiles", "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")
        
        response += "Sensitive value '" + escape(input_data.decode('utf-8')) + "' hashed and stored<br/>"
    except Exception as e:
        response += "Problem executing hash - TestCase"
        return response, 500

    response += "Hash Test executed"
    return response

class Test:
    def do_something(self, param):
        bar = escape(param)
        return bar

def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

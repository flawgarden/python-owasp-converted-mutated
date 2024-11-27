
from flask import Flask, request, render_template
import hashlib
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01759", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"
    param = request.form.get("BenchmarkTest01759")

    bar = Test().do_something(param)

    try:
        sha384 = hashlib.new('sha384')
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        else:
            response = "This input source requires a POST, not a GET. Incompatible UI for the InputStream source."
            return response

        sha384.update(input_data)
        result = sha384.digest()

        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response_output = "Sensitive value '" + escape_html(input_data.decode()) + "' hashed and stored<br/>"
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e)

    response_output += "Hash Test executed"
    return response_output

class Test:

    def do_something(self, param):
        return escape_html(param)

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01579", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.getlist('BenchmarkTest01579')
    if param:
        param = param[0]
    else:
        param = ""

    bar = Test().do_something(param)

    try:
        algorithm = "SHA512"
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md = hashlib.new(algorithm)
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + encode_for_base64(result) + b"\n")

        return (f"Sensitive value '{encode_for_html(input_data.decode())}' hashed and stored<br/>"
                f"Hash Test executed")

    except Exception as e:
        print("Problem executing hash - TestCase", e)
        return "Error processing request"

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the first safe value
            bar = values_list[0]  # get the param value

        return bar

def encode_for_base64(input_data):
    import base64
    return base64.b64encode(input_data).strip()

def encode_for_html(input_data):
    from markupsafe import escape
    return escape(input_data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

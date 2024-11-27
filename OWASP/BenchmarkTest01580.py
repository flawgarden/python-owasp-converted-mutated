
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01580", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest01580")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    try:
        algorithm = 'SHA512'
        md = hashlib.new(algorithm)
        input_data = b'?'
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('uploads/', 'passwordFile.txt')
        
        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + hash_to_base64(result) + b"\n")
        
        response += f"Sensitive value '{escape_html(input_data.decode())}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response += "Hash Test executed"
    return response

class Test:
    def do_something(self, param):
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

def hash_to_base64(data):
    import base64
    return base64.b64encode(data)

def escape_html(data):
    from html import escape
    return escape(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

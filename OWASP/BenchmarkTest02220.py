
from flask import Flask, request, render_template
import os
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02220", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    response = app.response_class(
        response="Method Not Allowed",
        status=405,
    )
    return response

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02220', '')

    bar = do_something(param)

    try:
        algorithm = 'SHA5'  # Placeholder for the hash algorithm logic
        if algorithm == 'SHA5':
            algorithm = 'sha256'
        
        md = hashlib.new(algorithm)
        input_data = bar.encode() if isinstance(bar, str) else bar
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("uploads", "passwordFile.txt")
        
        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + base64.b64encode(result) + b"\n")
        
        response.set_data(f"Sensitive value '{html_escape(input_data.decode())}' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash - TestCase", e)
        response.set_data("Internal Server Error")
        response.status_code = 500
        return response

    response.set_data("Hash Test executed")
    return response

def do_something(param):
    a19972 = param
    b19972 = a19972 + " SafeStuff"
    b19972 = b19972[:-1] + "Chars"
    map19972 = {'key19972': b19972}
    c19972 = map19972['key19972']
    d19972 = c19972[:-1]
    e19972 = base64.b64decode(base64.b64encode(d19972.encode())).decode()
    f19972 = e19972.split(" ")[0]

    # Placeholder for the ThingInterface logic
    bar = f19972  # In actual implementation, replace this with the interface logic

    return bar

def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

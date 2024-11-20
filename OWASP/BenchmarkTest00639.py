
import os
import base64
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00639", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = ''
    param = request.args.get('BenchmarkTest00639', '')

    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        algorithm = "SHA5"  # Default algorithm, replace with proper configuration handling if needed
        md = hashlib.new(algorithm)

        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode() + "\n")

        response += "Sensitive value '" + escape(input_param.decode()) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

    response += "Hash Test executed"
    return response

def escape(s):
    return ''.join(['&lt;' if c == '<' else '&gt;' if c == '>' else c for c in s])

if __name__ == "__main__":
    app.run(host='0.0.0.0')

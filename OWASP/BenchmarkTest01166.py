
import os
import urllib.parse
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01166", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""

    param = ""
    headers = request.headers.get('BenchmarkTest01166')

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        md = hashlib.new('sha1')
        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        response += "Sensitive value '{}' hashed and stored<br/>".format(escape_html(str(input_param)))

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response += "Hash Test executed"
    return response

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            sbxyz52006 = list(param)
            sbxyz52006[-1] = 'Z'
            bar = ''.join(sbxyz52006)

        return bar

def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

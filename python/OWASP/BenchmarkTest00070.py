
from flask import Flask, request, render_template, make_response
import hashlib
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00070", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-00/BenchmarkTest00070.html"))
        user_cookie = "BenchmarkTest00070=somesSecret"
        response.set_cookie('BenchmarkTest00070', 'someSecret', max_age=60*3, secure=True, path=request.path, domain=request.host)
        return response

    param = "noCookieValueSupplied"
    cookies = request.cookies

    if cookies and 'BenchmarkTest00070' in cookies:
        param = urllib.parse.unquote(cookies['BenchmarkTest00070'])

    bar = param
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        md = hashlib.sha1()
        input_bytes = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_bytes = input_param.encode()
        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join("path/to/your/test/files", "passwordFile.txt")
        
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_bytes.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - Exception occurred")
        raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')

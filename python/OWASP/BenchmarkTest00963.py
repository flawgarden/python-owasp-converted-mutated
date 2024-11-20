
import os
import hashlib
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00963", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-01/BenchmarkTest00963.html"))
        user_cookie = make_response("someSecret")
        response.set_cookie("BenchmarkTest00963", "someSecret", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00963" in cookies:
            param = unquote(cookies["BenchmarkTest00963"])

        bar = Test().do_something(param)

        try:
            md5_hash = hashlib.md5()
            input_data = b'?'
            input_param = bar
            if isinstance(input_param, str):
                input_data = input_param.encode()
            md5_hash.update(input_data)

            result = md5_hash.digest()
            file_target = os.path.join("path/to/test/files", "passwordFile.txt")
            with open(file_target, 'a') as fw:
                fw.write("hash_value=" + result.hex() + "\n")
            return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

        except Exception as e:
            print("Problem executing hash - TestCase")
            raise e

    return "Hash Test executed"

class Test:

    def do_something(self, param):
        bar = param  # In a real application, you would sanitize or encode this properly in production.
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

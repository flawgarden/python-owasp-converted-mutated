
import os
import hashlib
from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00071", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-00/BenchmarkTest00071.html"))
        user_cookie = "BenchmarkTest00071=someSecret; Max-Age=180; Secure; Path={}; Domain={}".format(request.path, request.host)
        response.set_cookie("BenchmarkTest00071", "someSecret", max_age=180, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00071" in cookies:
            param = cookies["BenchmarkTest00071"]

        bar = param

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        try:
            input_bytes = bar.encode()
            md = hashlib.new('sha1')
            md.update(input_bytes)

            result = md.digest()
            file_target = os.path.join('path_to_testfiles', 'passwordFile.txt')
            with open(file_target, 'a') as fw:
                fw.write("hash_value={}\n".format(result.hex()))  # Hexadecimal representation of the hash

            return "Sensitive value '{}' hashed and stored<br/>".format(input_bytes.decode())

        except Exception as e:
            print("Problem executing hash - TestCase")
            raise e

    return "Hash Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

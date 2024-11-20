
import os
import hashlib
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00966", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-01/BenchmarkTest00966.html"))
        user_cookie = "BenchmarkTest00966=someSecret"
        response.set_cookie("BenchmarkTest00966", "someSecret", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    param = "noCookieValueSupplied"
    if 'BenchmarkTest00966' in request.cookies:
        param = request.cookies.get("BenchmarkTest00966")

    bar = Test().do_something(request, param)

    try:
        algorithm = "SHA5"  # Mocking the algorithm, change as needed.
        md = hashlib.new(algorithm)
        input_data = b'?'  # Placeholder
        if isinstance(bar, str):
            input_data = bar.encode()
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/directory", "passwordFile.txt")

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")  # Store the hash in hex format

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>" + \
               "Hash Test executed"
    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

class Test:
    def do_something(self, request, param):
        num = 106
        bar = param if (7 * 42) - num <= 200 else "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

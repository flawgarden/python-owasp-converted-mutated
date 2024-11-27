
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01168", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get('BenchmarkTest01168')
    if headers:
        param = headers

    param = param  # URL decoding is handled by Flask

    bar = Test().do_something(request, param)

    try:
        algorithm = "SHA512"  # Default algorithm
        md = hashlib.new(algorithm)

        input_param = bar.encode('utf-8')
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('uploads/', 'passwordFile.txt')

        with open(file_target, 'ab') as fw:
            fw.write(b"hash_value=" + result + b"\n")

        return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ('C', 'D'):
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

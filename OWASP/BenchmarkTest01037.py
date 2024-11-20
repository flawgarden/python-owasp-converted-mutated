
import os
from flask import Flask, request, render_template
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01037", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01037", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    try:
        sha512 = hashlib.new("sha512")
        input_data = bar.encode() if isinstance(bar, str) else bar
        sha512.update(input_data)

        result = sha512.digest()
        file_target = os.path.join(os.getcwd(), "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + str(result.hex()) + "\n")

        return (f"Sensitive value '{input_data.decode()}' hashed and stored<br/>")

    except Exception as e:
        return f"Problem executing hash - {str(e)}"

class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ('C', 'D'):
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest01760", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.values.get("BenchmarkTest01760")
    bar = Test().do_something(param)

    try:
        md = hashlib.new("sha384")
        input_data = bar.encode('utf-8')
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join("path/to/directory", "passwordFile.txt")

        with open(file_target, 'a') as fw:  # the 'a' will append the new data
            fw.write("hash_value=" + base64.b64encode(result).decode('utf-8') + "\n")

        return f"Sensitive value '{html_escape(input_data.decode('utf-8'))}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new()")
        return str(e)

class Test:

    def do_something(self, param):
        guess = "ABC"
        switch_target = guess[2]

        # Simple case statement that assigns param to bar on conditions 'A', 'C', or 'D'
        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

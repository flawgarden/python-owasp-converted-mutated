
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01411", methods=['GET', 'POST'])
def benchmark_test_01411():
    if request.method == 'GET':
        return benchmark_test_01411_post()

    return benchmark_test_01411_post()

def benchmark_test_01411_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01411":
                    param = name
                    flag = False

    bar = Test().do_something(param)

    try:
        md = hashlib.sha1()
        input_param = bar.encode() if isinstance(bar, str) else bar

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('uploads/', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha1()")
        raise e

class Test:

    def do_something(self, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

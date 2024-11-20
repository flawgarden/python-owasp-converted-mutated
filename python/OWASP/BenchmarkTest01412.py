
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01412", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    for name in request.values.keys():
        values = request.values.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01412":
                    param = name
                    flag = False
                    break

    bar = Test().do_something(request, param)

    try:
        sha512 = hashlib.sha512()
        input_param = bar.encode('utf-8')
        sha512.update(input_param)

        result = sha512.digest()
        file_target = os.path.join('path/to/testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:  # the true will append the new data
            fw.write("hash_value=" + result.hex() + "\n")

        return render_template("index.html", message="Sensitive value '" + str(input_param.decode('utf-8')) + "' hashed and stored<br/>")
        
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

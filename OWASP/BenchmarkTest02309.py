
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02309", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest02309":
                    param = name
                    flag = False

    bar = do_something(param)

    try:
        import hashlib
        sha512 = hashlib.new('sha512')
        input_param = bar.encode('utf-8') if isinstance(bar, str) else bar
        sha512.update(input_param)

        result = sha512.digest()
        file_target = os.path.join('path/to/testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + str(result.hex()) + "\n")
        
        return "Sensitive value '{}' hashed and stored<br/>".format(input_param.decode())

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha512')")
        raise e

def do_something(param):
    # Simple ? condition that assigns param to bar on false condition
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

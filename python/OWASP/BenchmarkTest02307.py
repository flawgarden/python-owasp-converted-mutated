
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02307", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02307":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    try:
        md = hashlib.new('sha1')
        input_data = bar.encode('utf-8') if isinstance(bar, str) else bar
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={result.hex()}\n")

        return f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash.")
        return str(e)

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

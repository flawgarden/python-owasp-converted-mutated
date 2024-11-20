
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01246", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)

    return do_post(request)

def do_post(request):
    response = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest01246", "")
    bar = Test().do_something(request, param)

    try:
        md = hashlib.new('sha1')
        input_param = bar.encode() if isinstance(bar, str) else bar

        md.update(input_param)

        result = md.digest()
        file_target = os.path.join("path_to_your_testfiles_dir", "passwordFile.txt")

        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response_str = f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        raise e

    response_str += "Hash Test executed"
    return response_str

class Test:

    def do_something(self, request, param):
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')

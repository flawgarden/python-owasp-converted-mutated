
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01245", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = {}
    param = request.args.get("BenchmarkTest01245", "")
    bar = Test().do_something(param)

    try:
        md = hashlib.new('sha384')
        input_data = bar.encode('utf-8')

        md.update(input_data)
        result = md.digest()
        file_target = os.path.join(os.getcwd(), "passwordFile.txt")

        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response['message'] = f"Sensitive value '{input_data.decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        raise e

    response['confirmation'] = "Hash Test executed"
    return render_template("index.html", response=response)

class Test:
    def do_something(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

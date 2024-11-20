
import os
from flask import Flask, request, render_template
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02119", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = "text/html;charset=UTF-8"

    param = request.values.get("BenchmarkTest02119", "")
    bar = do_something(param)

    try:
        md = hashlib.sha512()
        input_value = bar.encode('utf-8')
        md.update(input_value)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, "a") as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response_content = "Sensitive value '{}' hashed and stored<br/>".format(input_value.decode('utf-8'))

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.sha512")
        raise Exception(e)

    response_content += "Hash Test hashlib.sha512 executed"
    return response_content

def do_something(param):
    bar = "safe!"
    map_70096 = {}
    map_70096["keyA-70096"] = "a-Value"
    map_70096["keyB-70096"] = param
    map_70096["keyC"] = "another-Value"
    bar = map_70096["keyB-70096"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

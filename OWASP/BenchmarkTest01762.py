
from flask import Flask, request, render_template
import hashlib
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01762", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = "text/html;charset=UTF-8"
    param = request.values.get("BenchmarkTest01762")
    
    bar = Test().do_something(param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()
            
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        return render_template("index.html", message="Sensitive value '" + bar + "' hashed and stored<br/>")

    except Exception as e:
        return "Problem executing hash - TestCase", 500

class Test:

    def do_something(self, param):
        bar = "default value"
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

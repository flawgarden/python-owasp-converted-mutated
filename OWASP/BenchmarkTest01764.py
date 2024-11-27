
import os
import hashlib
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest01764", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = ""
    param = request.values.get("BenchmarkTest01764")

    bar = Test().do_something(request, param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        input_param = bar
        if isinstance(input_param, str):
            input_data = input_param.encode()
        elif hasattr(input_param, 'read'):
            str_input = input_param.read(1000)
            if not str_input:
                return "This input source requires a POST, not a GET. Incompatible UI for the InputStream source."
            input_data = str_input

        md.update(input_data)
        result = md.digest()

        file_target = os.path.join("path_to_your_directory", "passwordFile.txt")
        with open(file_target, 'a') as fw:  # 'a' will append the new data
            fw.write("hash_value=" + result.hex() + "\n")
        
        response += "Sensitive value '" + secure_filename(input_data.decode('utf-8')) + "' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response += "Hash Test executed"
    return response

class Test:

    def do_something(self, request, param):
        bar = param.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

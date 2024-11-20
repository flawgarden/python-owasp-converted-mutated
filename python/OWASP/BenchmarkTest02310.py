
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02310", methods=['GET', 'POST'])
def benchmark_test():
    response_content = ""
    if request.method == 'POST' or request.method == 'GET':
        param = ""
        flag = True
        names = request.args if request.method == 'GET' else request.form
        for name in names:
            if flag:
                values = names.getlist(name)
                if values:
                    for value in values:
                        if value == "BenchmarkTest02310":
                            param = name
                            flag = False

        bar = do_something(param)

        try:
            md = hashlib.new('sha512')
            input_param = bar.encode() if isinstance(bar, str) else bar
            
            md.update(input_param)

            result = md.digest()
            file_target = os.path.join('path/to/directory/', 'passwordFile.txt')
            with open(file_target, 'a') as fw:
                fw.write("hash_value=" + str(result.hex()) + "\n")
            response_content += (
                "Sensitive value '" + escape_html(str(input_param)) + "' hashed and stored<br/>"
            )
        except Exception as e:
            print("Problem executing hash - TestCase hashlib.new('sha512')")
            raise e

        response_content += "Hash Test executed"
    return response_content

def do_something(param):
    bar = ""
    if param:
        bar = param.split(" ")[0]
    return bar

def escape_html(value):
    return value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

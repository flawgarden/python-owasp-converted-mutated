
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02312", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = "text/html;charset=UTF-8"
    param = ""
    flag = True

    for name in request.args.keys():
        values = request.values.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02312":
                    param = name
                    flag = False
                    break
            if not flag:
                break

    bar = do_something(param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path_to_your_testfiles_directory', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return "Sensitive value '" + escape_html(str(input_data)) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase")
        return str(e), 500

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")
        bar = values_list[0]

    return bar

def escape_html(s):
    return (s.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

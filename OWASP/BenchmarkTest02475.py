
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-02/BenchmarkTest02475", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest02475")
    param = values[0] if values else ""

    bar = do_something(param)

    try:
        md = hashlib.md5()
        input_param = bar.encode('utf-8')
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        response.data = "Sensitive value '{}' hashed and stored<br/>".format(escape_html(input_param.decode()))

    except Exception as e:
        print("Problem executing hash - TestCase")
        raise e

    response.data += "Hash Test executed"
    return response

def do_something(param):
    bar = "safe!"
    map_43776 = {}
    map_43776["keyA-43776"] = "a-Value"
    map_43776["keyB-43776"] = param
    map_43776["keyC"] = "another-Value"
    bar = map_43776["keyB-43776"]

    return bar

def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

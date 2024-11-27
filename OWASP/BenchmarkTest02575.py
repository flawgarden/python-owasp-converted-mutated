
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest02575", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02575="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02575' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = param.replace('%20', ' ')

    bar = do_something(param)

    try:
        md = hashlib.md5()
        input_data = bar.encode() if isinstance(bar, str) else bar
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')

        with open(file_target, 'ab') as fw:  # 'ab' to append binary data
            fw.write(b"hash_value=" + encode_for_base64(result) + b"\n")

        return f"Sensitive value '{encode_for_html(input_data.decode())}' hashed and stored<br/>"
    
    except Exception as e:
        print("Problem executing hash - TestCase", str(e))
        return str(e)

def do_something(param):
    bar = param
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    return bar

def encode_for_base64(data):
    import base64
    return base64.b64encode(data)

def encode_for_html(data):
    from html import escape
    return escape(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import os
import urllib.parse
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00791", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)

    return do_post(request)

def do_post(request):
    response = "text/html;charset=UTF-8"

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00791="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00791' in query string."

    param = query_string[param_loc + len(paramval):]

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = escape_html(param)

    try:
        md = hashlib.new("sha512")
        input_data = b'?'
        input_param = bar

        if isinstance(input_param, str):
            input_data = input_param.encode()

        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path/to/testfiles', 'passwordFile.txt')

        with open(file_target, 'a') as fw:
            fw.write(
                "hash_value=" + base64.b64encode(result).decode() + "\n"
            )

        return "Sensitive value '" + escape_html(input_data.decode()) + "' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new()")
        raise e

    return "Hash Test hashlib.new() executed"

def escape_html(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;"))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

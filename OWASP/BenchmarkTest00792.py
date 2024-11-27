
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00792", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)

    return do_post(request)

def do_post(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00792="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00792' in query string."

    param = query_string[param_loc + len(paramval):]  # get the value after the parameter

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval): ampersand_loc]

    param = param.replace('%20', ' ')  # Decode URL-encoded strings

    bar = "safe!"
    map_53005 = {}
    map_53005["keyA-53005"] = "a_Value"
    map_53005["keyB-53005"] = param
    map_53005["keyC"] = "another_Value"

    bar = map_53005["keyB-53005"]
    bar = map_53005["keyA-53005"]

    try:
        md = hashlib.new('sha512')
        input_data = bar.encode('utf-8') if isinstance(bar, str) else bar
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join('path/to/your/testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")

        return "Sensitive value '{}' hashed and stored<br/>".format(input_data.decode('utf-8'))

    except Exception as e:
        print("Problem executing hash - TestCase hashlib.new('sha512')")
        raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')

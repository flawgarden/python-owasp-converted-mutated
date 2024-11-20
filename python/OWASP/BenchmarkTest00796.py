
import os
import hashlib
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-00/BenchmarkTest00796", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = ''
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00796="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response += f"getQueryString() couldn't find expected parameter 'BenchmarkTest00796' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = unquote(param)

    bar = "safe!"
    map72213 = {
        "keyA-72213": "a-Value",
        "keyB-72213": param,
        "keyC": "another-Value"
    }
    bar = map72213["keyB-72213"]

    try:
        algorithm = "SHA512"
        md = hashlib.new(algorithm)
        input_param = bar.encode()
        md.update(input_param)

        result = md.digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        response += f"Sensitive value '{input_param.decode()}' hashed and stored<br/>"

    except Exception as e:
        response += "Problem executing hash - TestCase"
        return response

    response += "Hash Test executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

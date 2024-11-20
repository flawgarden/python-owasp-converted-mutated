
import os
from flask import Flask, request, render_template
import urllib.parse
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest01655", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01655="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01655' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
        
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        algorithm = 'SHA5'  # this should come from your properties if needed
        md = hashlib.new(algorithm)
        input_bytes = b'?'

        if isinstance(bar, str):
            input_bytes = bar.encode()
        
        md.update(input_bytes)

        result = md.digest()
        file_target = os.path.join('uploads', 'passwordFile.txt')
        with open(file_target, 'ab') as fw:
            fw.write(f"hash_value={result.hex()}\n".encode())
        
        return f"Sensitive value '{escape_html(str(input_bytes))}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash - TestCase", e)
        return str(e)

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class Test:
    def do_something(self, request, param):
        bar = None

        # Simple if statement that assigns param to bar on true condition
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

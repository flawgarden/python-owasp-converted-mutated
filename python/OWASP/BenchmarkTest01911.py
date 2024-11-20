
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01911", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.headers.get('BenchmarkTest01911', '')

    param = param  # No need for URL decoding, Flask handles this

    bar = do_something(param)

    try:
        md = hashlib.new('sha1')
        input_param = bar.encode() if isinstance(bar, str) else bar
        md.update(input_param)

        result = md.digest()
        
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={result.hex()}\n")

        response.data = f"Sensitive value '{input_param.decode()}' hashed and stored<br/>".encode()
    except Exception as e:
        response.data = f"Problem executing hash: {str(e)}".encode()
        return response

    response.data += "Hash Test executed".encode()
    return response

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

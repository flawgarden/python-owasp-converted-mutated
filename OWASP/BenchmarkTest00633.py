
import os
from flask import Flask, request, render_template
import hashlib
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, name):
        return self.request.args.get(name)

@app.route("/hash-00/BenchmarkTest00633", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00633")
    if param is None:
        param = ""

    bar = None
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    try:
        hash_value = hashlib.sha384(bar.encode()).digest()
        file_target = os.path.join('testfiles', 'passwordFile.txt')
        
        with open(file_target, 'a') as fw:
            fw.write(f"hash_value={base64.b64encode(hash_value).decode()}\n")
            
        return f"Sensitive value '{base64.b64encode(param.encode()).decode()}' hashed and stored<br/>"

    except Exception as e:
        print("Problem executing hash")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

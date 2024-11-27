
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00567", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = "text/html;charset=UTF-8"
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00567":
                    param = name
                    flag = False
                    break
        if not flag:
            break
    
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = ""
    if "Windows" in os.name:
        cmd = "echo "

    try:
        p = os.popen(cmd + bar)
        output = p.read()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

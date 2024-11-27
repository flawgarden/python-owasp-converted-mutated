
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00171", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    param = request.headers.get('BenchmarkTest00171', '')
    
    param = urllib.parse.unquote(param)

    bar = "safe!"
    map40534 = {
        "keyA-40534": "a_Value",
        "keyB-40534": param,
        "keyC": "another_Value"
    }
    bar = map40534["keyB-40534"]
    bar = map40534["keyA-40534"]

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))
        response.data = process.read()
        response.mimetype = 'text/html;charset=UTF-8'
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e).encode('utf-8')
        response.mimetype = 'text/html;charset=UTF-8'
    
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, render_template
import os
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00906", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = render_template("index.html")
    
    param = request.args.get('BenchmarkTest00906')
    bar = ""
    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = ""
    a1 = ""
    a2 = ""
    args = []
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo"
        args = [a1, a2, cmd, bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ping -c1 "
        args = [a1, a2, cmd + bar]

    try:
        output = os.popen(' '.join(args)).read()
        response += "<pre>" + output + "</pre>"
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response += "<pre>" + str(e) + "</pre>"
    
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

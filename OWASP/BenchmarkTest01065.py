
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        num = 86
        if (7 * 42) - num > 200:
            return "This_should_always_happen"
        return param

@app.route("/cmdi-01/BenchmarkTest01065", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = request.headers.get("BenchmarkTest01065", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

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
        cmd = "ping -c 1 "
        args = [a1, a2, cmd + bar]

    try:
        result = os.popen(' '.join(args)).read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

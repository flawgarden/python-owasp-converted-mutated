
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01529", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01529", "")
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
        cmd = "ping -c1 "
        args = [a1, a2, cmd + bar]

    try:
        process = os.popen(' '.join(args))
        results = process.read()
        return render_template("results.html", results=results)
    except Exception as e:
        return render_template("error.html", error=str(e))

class Test:
    def do_something(self, param):
        num = 106
        return "This_should_always_happen" if (7 * 18) + num > 200 else param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

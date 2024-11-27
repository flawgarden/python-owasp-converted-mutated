
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00406", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00406", "")
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == "nt":
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
        process = os.execvp(args[0], args)
        return process
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error_message=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

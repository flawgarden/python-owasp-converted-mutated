
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00739", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = request

    values = request.args.getlist('BenchmarkTest00739')
    param = values[0] if values else ""

    bar = ""

    num = 106

    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

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
        output = process.read()
        return render_template("index.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("index.html", error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

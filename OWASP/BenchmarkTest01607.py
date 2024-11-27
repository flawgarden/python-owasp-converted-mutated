
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01607", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest01607")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
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
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        response = output.decode() + error.decode()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = str(e)

    return response

class Test:
    def do_something(self, param):
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

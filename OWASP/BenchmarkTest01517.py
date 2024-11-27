
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01517", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ''
    param = request.form.get('BenchmarkTest01517', '')

    bar = Test().do_something(request, param)

    a1, a2 = ("cmd.exe", "/c") if "Windows" in os.name else ("sh", "-c")
    args = [a1, a2, f"echo {bar}"]

    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        response = stdout.decode() if stdout else stderr.decode()
    except Exception as e:
        print("Problem executing command")
        raise Exception(e)

    return render_template("response.html", output=response)

class Test:
    def do_something(self, request, param):
        bar = ""

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

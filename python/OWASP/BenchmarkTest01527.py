
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01527", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01527", "")

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Check for Windows
        cmd = "echo "

    try:
        process = subprocess.Popen(cmd + bar, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode('utf-8') if output else error.decode('utf-8')
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:
    def do_something(self, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

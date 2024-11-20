
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01443", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01443":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "echo"

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + " " + bar)
        result = process.read()
        print(result)  # Assuming this prints results to output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return "Error: " + str(e)

class Test:

    def do_something(self, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

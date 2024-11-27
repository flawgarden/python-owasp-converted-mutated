
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01269", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.values.get("BenchmarkTest01269", "")
    bar = Test().do_something(param)

    a1 = "cmd.exe" if "Windows" in os.name else "sh"
    a2 = "/c" if "Windows" in os.name else "-c"
    args = [a1, a2, f"echo {bar}"]

    try:
        process = os.popen(' '.join(args))
        result = process.read()
        return result
    except Exception as e:
        print("Problem executing command")
        return str(e)

class Test:
    def do_something(self, param):
        num = 86
        if (7 * 42) - num > 200:
            return "This_should_always_happen"
        return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')

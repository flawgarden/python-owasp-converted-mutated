
import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/cmdi-02/BenchmarkTest02496", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_html = ""
    values = request.values.getlist("BenchmarkTest02496")
    param = values[0] if values else ""

    bar = do_something(param)

    a1 = "cmd.exe" if os.name == "nt" else "sh"
    a2 = "/c" if os.name == "nt" else "-c"
    args = [a1, a2, "echo " + bar]

    try:
        result = os.popen(' '.join(args)).read()
        response_html = result
    except Exception as e:
        print("Problem executing cmdi - subprocess execution error")
        raise e

    return response_html

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

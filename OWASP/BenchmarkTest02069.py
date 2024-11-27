
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02069", methods=['GET', 'POST'])
def benchmark_test_02069():
    if request.method == 'GET':
        return benchmark_test_02069_post()

    return benchmark_test_02069_post()

def benchmark_test_02069_post():
    response = app.response_class()
    param = request.headers.get('BenchmarkTest02069', '')

    param = param.encode('utf-8').decode('utf-8')

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # simple echo for Windows

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        results = process.read()
        response.data = results
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e).encode('utf-8')

    return response

def do_something(param):
    bar = None
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

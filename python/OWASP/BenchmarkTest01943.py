
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01943", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.headers.get('BenchmarkTest01943', '')
    param = param.encode('utf-8').decode('utf-8')

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing command")
        response.data = str(e)
        return response

def do_something(param):
    bar = "safe!"
    map_ = {"keyA-72345": "a_Value", "keyB-72345": param, "keyC": "another_Value"}
    bar = map_.get("keyB-72345")  # get it back out
    bar = map_.get("keyA-72345")  # get safe value back out

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

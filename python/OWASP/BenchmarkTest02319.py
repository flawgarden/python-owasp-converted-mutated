
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02319", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response_headers = {'X-XSS-Protection': '0'}
    param = ""
    flag = True
    names = request.args

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02319":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(request, param)
    
    return bar, 200, response_headers

def do_something(request, param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

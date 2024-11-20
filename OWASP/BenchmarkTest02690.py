
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02690", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class(mimetype='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest02690") if request.method == 'GET' else request.form.get("BenchmarkTest02690")
    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    return response

def do_something(request, param):
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

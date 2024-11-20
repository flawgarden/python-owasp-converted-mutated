
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/xss-04/BenchmarkTest02240", methods=['GET', 'POST'])
def benchmark_test_02240():
    if request.method == 'GET':
        return benchmark_test_02240_post()
    return benchmark_test_02240_post()

def benchmark_test_02240_post():
    param = request.args.get('BenchmarkTest02240', '')
    bar = do_something(param)

    response = app.response_class(
        response=bar,
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

def do_something(param):
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

if __name__ == '__main__':
    app.run(host='0.0.0.0')

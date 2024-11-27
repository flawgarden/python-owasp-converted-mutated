
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01957", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    param = request.headers.get("BenchmarkTest01957", "")

    param = param.encode('utf-8').decode('utf-8')

    bar = do_something(param)

    request.environ['wsgi.session'][bar] = "10340"

    return f"Item: '{bar}' with value: 10340 saved in session."

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

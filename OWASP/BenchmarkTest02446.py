
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02446", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest02446", "")
    bar = do_something(param)

    # Simulating session storage
    request.environ['werkzeug.server.shutdown']()
    session = request.session
    session[bar] = "10340"

    return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

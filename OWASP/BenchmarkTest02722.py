
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02722", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest02722")
    bar = do_something(param)

    # Simulating session storage
    request.environ['beaker.session'][bar] = "10340"

    return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

def do_something(param):
    # Simulating ESAPI encoding for HTML
    bar = encode_for_html(param)
    return bar

def encode_for_html(value):
    # Simple HTML encoding function
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

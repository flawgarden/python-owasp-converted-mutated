
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02726", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest02726')

    bar = do_something(request, param)

    # Save 'userid' in session
    request.environ['werkzeug.session'].modify({"userid": bar})

    response.data = f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."
    return response

def do_something(request, param):
    bar = param
    if param is not None and len(param) > 1:
        bar = param[:-1]
    return bar

def encode_for_html(value):
    if value is None:
        return ''
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

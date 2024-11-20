
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02165", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    
    param = request.args.get('BenchmarkTest02165', '')

    bar = do_something(param)

    request.environ['wsgi.session'][bar] = '10340'

    return "Item: '{}' with value: 10340 saved in session.".format(encode_for_html(bar))

def do_something(param):
    bar = encode_for_html(param)
    return bar

def encode_for_html(param):
    return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

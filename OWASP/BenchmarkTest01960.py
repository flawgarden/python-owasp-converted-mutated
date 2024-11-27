
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01960", methods=['GET', 'POST'])
def benchmark_test_01960():
    if request.method == 'GET':
        return benchmark_test_01960_post(request)

    return benchmark_test_01960_post(request)

def benchmark_test_01960_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    if request.headers.get('BenchmarkTest01960') is not None:
        param = request.headers.get('BenchmarkTest01960')

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    request.session['userid'] = bar

    response.data = "Item: 'userid' with value: '{}' saved in session.".format(encode_for_html(bar))
    return response

def do_something(request, param):
    bar = param
    if param is not None and len(param) > 1:
        bar = param[:-1]
    return bar

def encode_for_html(value):
    from html import escape
    return escape(value)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

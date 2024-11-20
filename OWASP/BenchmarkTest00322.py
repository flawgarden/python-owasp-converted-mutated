
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00322", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = ''
    headers = request.headers.get('BenchmarkTest00322')

    if headers:
        param = headers

    param = param

    bar = "safe!"
    map53101 = {
        "keyA-53101": "a_Value",
        "keyB-53101": param,
        "keyC": "another_Value"
    }
    bar = map53101.get("keyB-53101")
    bar = map53101.get("keyA-53101")

    request.environ['werkzeug.session']['userid'] = bar

    return response.set_data(
        "Item: 'userid' with value: '{}' saved in session.".format(bar)
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')

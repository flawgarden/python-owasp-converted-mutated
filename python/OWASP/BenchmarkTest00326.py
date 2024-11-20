
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00326", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    headers = request.headers.getlist("BenchmarkTest00326")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    # Simulating session attribute storage
    request.environ['werkzeug.session']['bar'] = "10340"

    response.data = f"Item: '{bar}' with value: '10340' saved in session.".encode('utf-8')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

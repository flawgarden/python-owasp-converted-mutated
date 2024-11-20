
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01916", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if 'Referer' in request.headers:
        param = request.headers['Referer']

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    return response

def do_something(param):
    bar = ""
    if param:
        bar = param.split(" ")[0]

    return bar

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01925", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("Referer") is not None:
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        sbxyz28389 = list(param)
        sbxyz28389[-1] = "Z"
        bar = ''.join(sbxyz28389)
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01915", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.headers.get("Referer") is not None:
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data("Formatted like: %s and %s." % ("a", bar))
    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

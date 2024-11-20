
import urllib.parse
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02050", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    referer = request.headers.get("Referer")
    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    obj = ("a", bar)
    response.data = "Formatted like: {} and {}.".format(*obj)

    return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

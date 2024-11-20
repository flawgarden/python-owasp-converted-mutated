
from flask import Flask, request, Response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01914", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return do_post(request)

def do_post(request):
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.headers.get("Referer"):
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.set_data(f"<!DOCTYPE html>\n<html>\n<body>\n<p>Formatted like: {obj[0]} and {obj[1]}.\n</p>\n</body>\n</html>")
    return response

def do_something(request, param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

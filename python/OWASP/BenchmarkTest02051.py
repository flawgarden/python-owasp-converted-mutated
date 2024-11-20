
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02051", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    referer = request.headers.get('Referer')

    if referer:
        param = referer  # just grab the Referer header

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = f"Formatted like: {bar} and b."
    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
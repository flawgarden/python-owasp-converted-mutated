
from flask import Flask, request, Response
import urllib.parse
from werkzeug.utils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01048", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get('Referer', '')
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar.format("a", "b").encode('utf-8')
    return response

class Test:

    def do_something(self, request, param):
        bar = escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

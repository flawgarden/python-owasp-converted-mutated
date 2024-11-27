
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01053", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get('Referer', '')
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

class Test:

    def do_something(self, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')

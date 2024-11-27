
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01054", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.headers.get('Referer', '')
        param = urllib.parse.unquote(param)

        bar = Test().do_something(param)

        response.headers['X-XSS-Protection'] = '0'
        response.set_data(bar)
        return response

class Test:

    def do_something(self, param):
        bar = urllib.parse.quote(param, safe='')
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')


from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01050", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('Referer', '')
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response = make_response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:
    def do_something(self, request, param):
        sbxyz75528 = str(param)
        bar = sbxyz75528 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

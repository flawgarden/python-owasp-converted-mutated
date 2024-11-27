
import os
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01349", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.values.get('BenchmarkTest01349', '')

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

class Test:
    def do_something(self, param):
        sbxyz63030 = str(param)
        bar = sbxyz63030 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

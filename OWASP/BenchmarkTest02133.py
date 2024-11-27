
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02133", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    if request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest02133', '')
    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

def do_something(param):
    bar = ''

    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')


from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02237", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.args.get('BenchmarkTest02237', '')

        bar = do_something(param)

        response.headers['X-XSS-Protection'] = '0'
        response.data = bar
        return response

def do_something(param):
    from html import escape
    bar = escape(param)
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

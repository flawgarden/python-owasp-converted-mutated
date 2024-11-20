
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02131", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        response = make_response()
        response.content_type = "text/html;charset=UTF-8"

        param = request.args.get('BenchmarkTest02131', default='', type=str)
        bar = do_something(param)

        response.headers['X-XSS-Protection'] = '0'
        obj = ["a", "b"]
        response.data = bar % tuple(obj)

        return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')

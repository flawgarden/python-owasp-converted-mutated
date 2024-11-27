
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02494", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    values = request.args.getlist("BenchmarkTest02494")
    param = values[0] if values else ""

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        sbxyz57919 = list(param)
        sbxyz57919[-1] = 'Z'
        bar = ''.join(sbxyz57919)

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
